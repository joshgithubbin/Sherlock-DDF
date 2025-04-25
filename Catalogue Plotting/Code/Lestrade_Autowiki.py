#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 21:02:48 2025

@author: joshuaweston
"""

import requests
import re
import pandas as pd
import os

# Function to extract the abstract from the ReadMe file
def get_abstract(content):
    abstract_match = re.search(
        r"(?<=Abstract:\n)(.*?)(?=\n[A-Z][^\n]{5,})",
        content,
        re.DOTALL
    )

    if abstract_match:
        raw_abstract = abstract_match.group(1)
        cleaned_abstract = re.sub(r"\n\s+", " ", raw_abstract)  # join lines
        cleaned_abstract = re.sub(r" {2,}", " ", cleaned_abstract)  # remove extra spaces
        cleaned_abstract = cleaned_abstract.strip()
    else:
        cleaned_abstract = "Abstract section not found."
    
    return f"## Summary\n\n{cleaned_abstract}\n"

# Function to extract the tables and notes from the ReadMe file
def get_tables_and_notes(content):
    table_matches = re.findall(
        r"(Byte-by-byte Description of file: [^\n]+(?:\n.*?)+?)\n{2,}",
        content,
        re.DOTALL
    )

    markdown_tables = []

    if table_matches:
        for idx, table_data in enumerate(table_matches, start=1):
            # Remove dashed lines
            table_data = re.sub(r"-{50,}", "", table_data)

            # Step 5: Extract rows from the table
            rows = re.findall(r"(\d+-\s*\d+|\d+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(.+)", table_data)

            # Step 6: Create a pandas DataFrame for each table
            table_df = pd.DataFrame(rows, columns=["Bytes", "Format", "Units", "Label", "Explanations"])

            # Step 7: Clean up 'Bytes' column
            table_df['Bytes'] = table_df['Bytes'].apply(lambda x: re.sub(r'\s+', ' ', x).strip())

            # Extract table name for summary label
            table_name_match = re.search(r"file: (\S+)", table_data)
            table_name = table_name_match.group(1) if table_name_match else f"table{idx}.dat"

            # Step 8: Extract notes for the table (including multi-line notes)
            note_match = re.search(r"Note\s*\(\d+\):\s*(.*?)(?=\n-{50,}|\n*$)", table_data, re.DOTALL)
            note_text = note_match.group(1).strip() if note_match else None

            # Convert the DataFrame to markdown format
            markdown_table = f"<details>\n<summary>{table_name} catalogue schema</summary>\n\n"
            markdown_table += table_df.to_markdown(index=False)
            
            # Append the note if available
            if note_text:
                markdown_table += f"\n\n**Note**: {note_text}\n"

            markdown_table += "\n</details>\n"

            # Store the markdown table
            markdown_tables.append(markdown_table)

    else:
        print("No tables found in the document.")
    
    return "\n".join(markdown_tables)

def has_morphology_info(content):
    morphology_keywords = ["semi-major axis", "semimajor axis", "major axis","A_IMAGE"]

    table_matches = re.findall(
        r"(Byte-by-byte Description of file: [^\n]+(?:\n.*?)+?)\n{2,}",
        content,
        re.DOTALL
    )

    if table_matches:
        for table_data in table_matches:
            table_data = re.sub(r"-{50,}", "", table_data)
            rows = re.findall(r"(\d+-\s*\d+|\d+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(.+)", table_data)

            for row in rows:
                explanation = row[4].lower()
                if any(keyword.lower() in explanation for keyword in morphology_keywords):
                    return True

    return False

def count_tables(content):
    return len(re.findall(r"Byte-by-byte Description of file:", content))

# Function to search for 'redshift' in the table explanations and return concatenated strings
def search_redshift_in_explanations(content):
    # Regex to find all rows (similar to what we use to extract tables)
    table_matches = re.findall(
        r"(Byte-by-byte Description of file: [^\n]+(?:\n.*?)+?)\n{2,}",
        content,
        re.DOTALL
    )

    # Lists to store categorized labels
    spectroscopic_redshift_labels = []
    photometric_redshift_labels = []
    redshift_qualities_labels = []
    other_redshift_metrics_labels = []

    if table_matches:
        for idx, table_data in enumerate(table_matches, start=1):
            # Remove dashed lines
            table_data = re.sub(r"-{50,}", "", table_data)

            # Extract rows (same as previous extraction)
            rows = re.findall(r"(\d+-\s*\d+|\d+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(.+)", table_data)

            for row in rows:
                label = row[3]
                explanation = row[4].strip()

                # Only process rows where the label contains 'z' and 'redshift' is mentioned in the explanation
                if 'z' in label.lower() and 'redshift' in explanation.lower():
                    # Check for specific categories
                    if 'qualit' in explanation.lower():
                        redshift_qualities_labels.append(label)
                    elif 'spec' in explanation.lower():
                        if label not in redshift_qualities_labels:  # Avoid duplicate entries in the qualities category
                            spectroscopic_redshift_labels.append(label)
                    elif 'phot' in explanation.lower():
                        if label not in redshift_qualities_labels:  # Avoid duplicate entries in the qualities category
                            photometric_redshift_labels.append(label)
                    else:
                        # Add to "OTHER" category only if it doesn't fall into the other categories
                        if label not in redshift_qualities_labels and label not in spectroscopic_redshift_labels and label not in photometric_redshift_labels:
                            other_redshift_metrics_labels.append(label)

                # Special case: If the label is just "z" or "zbest"
                if label.lower() == 'z' or label.lower() == 'zbest':
                    # If it exists in the spectroscopic category, remove from other categories and move to spectroscopic
                    if spectroscopic_redshift_labels:
                        if label in other_redshift_metrics_labels:
                            other_redshift_metrics_labels.remove(label)  # Remove from other category if it exists
                        if label in photometric_redshift_labels:
                            photometric_redshift_labels.remove(label)  # Remove from photometric category if it exists
                        spectroscopic_redshift_labels.append(label)  # Move to spectroscopic
                    else:
                        if label in other_redshift_metrics_labels:
                            other_redshift_metrics_labels.remove(label)  # Remove from other category if it exists
                        photometric_redshift_labels.append(label)  # Move to photometric

    # Remove duplicates by converting lists to sets, then back to lists
    spectroscopic_redshift_labels = list(set(spectroscopic_redshift_labels))
    photometric_redshift_labels = list(set(photometric_redshift_labels))
    redshift_qualities_labels = list(set(redshift_qualities_labels))
    other_redshift_metrics_labels = list(set(other_redshift_metrics_labels))

    # Concatenate labels into comma-separated strings
    spectroscopic_redshift_str = ", ".join(spectroscopic_redshift_labels)
    photometric_redshift_str = ", ".join(photometric_redshift_labels)
    redshift_qualities_str = ", ".join(redshift_qualities_labels)
    other_redshift_metrics_str = ", ".join(other_redshift_metrics_labels)
    
    # Return the concatenated strings
    return spectroscopic_redshift_str, photometric_redshift_str, redshift_qualities_str, other_redshift_metrics_str



def extract_type_flags(content):
    # Exact match keywords (case-insensitive)
    exact_keywords = ['AGN', 'S/G', 'G/S']

    # Substring match keywords (case-insensitive)
    substring_keywords = ['type', 'class']

    type_labels = []

    # Extract table sections
    table_matches = re.findall(
        r"(Byte-by-byte Description of file: [^\n]+(?:\n.*?)+?)\n{2,}",
        content,
        re.DOTALL
    )

    if table_matches:
        for table_data in table_matches:
            table_data = re.sub(r"-{50,}", "", table_data)

            rows = re.findall(r"(\d+-\s*\d+|\d+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(.+)", table_data)

            for row in rows:
                label = row[3]

                # Check exact matches
                if any(re.fullmatch(rf"{re.escape(kw)}", label, re.IGNORECASE) for kw in exact_keywords):
                    type_labels.append(label)

                # Check substring matches
                elif any(kw in label.lower() for kw in substring_keywords):
                    type_labels.append(label)

    return ", ".join(sorted(set(type_labels)))


# Function to generate markdown for each DOI
def generate_markdown(cdf, doi):
    url = f"https://cdsarc.cds.unistra.fr/ftp/{doi}/ReadMe"
    
    response = requests.get(url)

    if response.status_code == 200:
        content = response.text

        # Get abstract and tables/notes
        abstract_md = get_abstract(content)
        tables_and_notes_md = get_tables_and_notes(content)

        # Search for 'redshift' in table explanations and categorize them
        spectroscopic_redshift, photometric_redshift, redshift_qualities, other_redshift_metrics = search_redshift_in_explanations(content)
        # Extract type-related labels
        type_flags = extract_type_flags(content)
        has_morph = has_morphology_info(content)
        
        # Count number of tables and add to the DataFrame
        table_count = count_tables(content)

        # Combine and save markdown content
        markdown_content = abstract_md + "\n## Catalogue Schema\n\n" + tables_and_notes_md

        # Replace slashes with underscores in the DOI
        doi2 = doi.replace("/", "_")

        # Ensure the 'wikipages' folder exists
        if not os.path.exists('wikipages'):
            os.makedirs('wikipages')

        # Save the generated markdown content to a file in the 'wikipages' folder
        file_path = os.path.join('wikipages', f"wiki_{doi2}.md")
        with open(file_path, "w", encoding="utf-8") as md_file:
            md_file.write(markdown_content)

        print(f"\nMarkdown file saved to {file_path}")
        
        # Set default RA/Dec column names
        cdf.loc[cdf['ID'] == doi, 'RA Column'] = 'RAJ2000'
        cdf.loc[cdf['ID'] == doi, 'Dec Column'] = 'DEJ2000'
        
        cdf.loc[cdf['ID'] == doi, 'Total Tables.'] = table_count

        # Insert the lists into the DataFrame columns as string representations
        cdf.loc[cdf['ID'] == doi, 'spec_z'] = str(spectroscopic_redshift)
        cdf.loc[cdf['ID'] == doi, 'photo_z'] = str(photometric_redshift)
        cdf.loc[cdf['ID'] == doi, 'qual_z'] = str(redshift_qualities)
        cdf.loc[cdf['ID'] == doi, 'other_z'] = str(other_redshift_metrics)
        
        cdf.loc[cdf['ID'] == doi, 'Type_Flag'] = str(type_flags)
        cdf.loc[cdf['ID'] == doi, 'Morphology'] = has_morph
        

    else:
        print(f"Failed to download file. Status code: {response.status_code}")
    
    return cdf

# Read in the Catalogue List
cdf = pd.read_csv('../Catalogue_List.csv')

# For each DOI, generate markdown and update the DataFrame
for doi in cdf['ID']:
    generate_markdown(cdf, doi.strip())

# After processing all DOIs, save the updated DataFrame back to a new CSV file
cdf.to_csv('../Updated_Catalogue_List.csv', index=False)

print("Updated catalogue list saved successfully!")
