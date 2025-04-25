#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 15:57:23 2025

@author: joshuaweston
"""

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
from collections import defaultdict, Counter

def find_shared_columns(content):
    # Define exact matches (case-insensitive)
    exact_columns = ["RAdeg", "DEdeg", "RAJ2000", "DEJ2000", "SEQ"]
    
    # Regex for 'xxxSeqxxx' or 'xxxIDxxx' with <= 3 characters on either side
    seq_or_id_pattern = re.compile(r"^.{0,3}(seq|id).{0,3}$", re.IGNORECASE)

    # Match all Byte-by-byte table definitions
    table_matches = re.findall(
        r"(Byte-by-byte Description of file: ([^\n]+)(?:\n.*?)+?)\n{2,}",
        content,
        re.DOTALL
    )

    label_to_explanations = defaultdict(list)
    label_occurrences = defaultdict(int)
    always_include = set()

    def matches_criteria(label, explanation):
        label_lower = label.lower()
        if label_lower in (col.lower() for col in exact_columns):
            return True
        if seq_or_id_pattern.match(label):
            return True
        if (
            ("unique" in explanation.lower() or " id" in explanation.lower() or "index" in explanation.lower() or "name" in explanation.lower())
            and "quality" not in explanation.lower()
        ):
            return True
        return False

    if table_matches:
        for table_data, table_name in table_matches:
            table_data = re.sub(r"-{50,}", "", table_data)
            rows = re.findall(r"(\d+-\s*\d+|\d+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(.+)", table_data)

            for row in rows:
                label = row[3].strip()
                explanation = row[4].strip()

                if matches_criteria(label, explanation):
                    label_occurrences[label] += 1
                    label_to_explanations[label].append(explanation)

                    # If filename contains *, mark label to always include
                    if '*' in table_name:
                        always_include.add(label)

    # Shared if it occurs >1 times OR is in a wildcard-named schema
    shared_columns = [label for label in label_occurrences if label_occurrences[label] > 1 or label in always_include]

    return shared_columns

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
    """
    Count the number of actual data tables listed under the File Summary section,
    based on lines ending in `.dat`.
    """
    # Extract the File Summary block
    file_summary_match = re.search(
        r"-{10,}\n\s*FileName\s+Lrecl\s+Records\s+Explanations\s*\n-{10,}\n(.*?)(?=\n-{10,}|$)",
        content,
        re.DOTALL
    )

    if file_summary_match:
        file_block = file_summary_match.group(1)
        # Count lines that end in '.dat' (possibly with leading spaces)
        dat_lines = re.findall(r"^\s*\S+\.dat\b", file_block, re.MULTILINE)
        return len(dat_lines)

    return 0  # fallback if the file summary wasn't found


# Function to search for 'redshift' in the table explanations and return concatenated strings



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


def search_redshift_in_explanations(content):
    # Define keywords related to redshift and their categories
    redshift_keywords = ['z', 'zph', 'zsp', 'zbest', 'q_z', 'e_z', 'r_z', 'redshift']
    
    # Define categories for classification
    spectroscopic_keywords = ['spec']
    photometric_keywords = ['phot', 'template', 'hybrid', 'ML']
    quality_keywords = ['qualit']
    other_keywords = ['error', 'uncertainty', 'metric', 'measurement']

    # Initialize lists to store categorized redshift metrics
    spectroscopic_redshift_labels = []
    photometric_redshift_labels = []
    redshift_qualities_labels = []
    other_redshift_metrics_labels = []

    # Extract abstract
    abstract_match = re.search(r"Abstract:\s*(.*?)\n{2,}", content, re.DOTALL)
    abstract = abstract_match.group(1) if abstract_match else ""

    # Extract table sections
    table_matches = re.findall(
        r"(Byte-by-byte Description of file: [^\n]+(?:\n.*?)+?)\n{2,}",
        content,
        re.DOTALL
    )

    if table_matches:
        for idx, table_data in enumerate(table_matches, start=1):
            # Clean up dashed lines and extract rows
            table_data = re.sub(r"-{50,}", "", table_data)
            rows = re.findall(r"(\d+-\s*\d+|\d+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(.+)", table_data)

            # Combine explanations for labels that span multiple lines
            label_explanations = {}

            for row in rows:
                label = row[3]
                explanation = row[4].strip()

                # If this label already has an explanation, append the current one
                if label in label_explanations:
                    label_explanations[label] += " " + explanation
                else:
                    label_explanations[label] = explanation

            for label, full_explanation in label_explanations.items():
                # Skip if the label itself contains "mag" or the explanation contains "flux" or "magnitude"
                if "mag" in label.lower() or "flux" in full_explanation.lower() or "magnitude" in full_explanation.lower():
                    continue

                # First check for quality-related labels like "q_", "e_", and "r_"
                if "q_" in label.lower() or "e_" in label.lower() or "r_" in label.lower():
                    # Check if the label contains a redshift-related keyword
                    if any(keyword.lower() in label.lower() for keyword in redshift_keywords):
                        # Put in 'qual' category if it matches quality-related keywords
                        redshift_qualities_labels.append(label)
                    continue

                # Check if any redshift keyword appears in the label
                if any(keyword.lower() in label.lower() for keyword in redshift_keywords):
                    # Check for specific categories based on the explanation
                    if any(keyword.lower() in full_explanation.lower() for keyword in spectroscopic_keywords):
                        spectroscopic_redshift_labels.append(label)
                    elif any(keyword.lower() in full_explanation.lower() for keyword in photometric_keywords):
                        # Explicitly check for photometric redshift methods like Hybrid or ML
                        if 'hybrid' in full_explanation.lower() or 'ML' in full_explanation.lower():
                            photometric_redshift_labels.append(label)
                        else:
                            photometric_redshift_labels.append(label)
                    elif any(keyword.lower() in full_explanation.lower() for keyword in quality_keywords):
                        redshift_qualities_labels.append(label)
                    else:
                        # If it doesn't fit in other categories, classify as "other"
                        other_redshift_metrics_labels.append(label)

    # Now check for 'z' labels in the other category
    if 'z' in other_redshift_metrics_labels:
        # Check abstract for 'spec' and 'redshift'
        abstract_sentences = re.split(r'\.\s*', abstract)
        for sentence in abstract_sentences:
            if "spectro" in sentence.lower():
                # Move 'z' from other to spectroscopic redshift
                spectroscopic_redshift_labels.append('z')
                other_redshift_metrics_labels.remove('z')
                break
        else:
            # If 'spec' and 'redshift' are not found in the same sentence, move 'z' to photometric redshift
            photometric_redshift_labels.append('z')
            other_redshift_metrics_labels.remove('z')

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


def assign_best_redshift(cdf, doi):
    # Check if the DOI exists in the DataFrame
    if doi not in cdf['ID'].values:
        print(f"DOI {doi} not found in DataFrame.")
        return cdf  # Return the original DataFrame if DOI is not found

    # Retrieve the redshift columns (spec_z and photo_z)
    spec_z = cdf.loc[cdf['ID'] == doi, 'spec_z'].values
    photo_z = cdf.loc[cdf['ID'] == doi, 'photo_z'].values

    # If no redshift values are found, return the DataFrame as is
    if len(spec_z) == 0 or len(photo_z) == 0:
        print(f"Redshift values not found for DOI {doi}.")
        return cdf

    spec_z = spec_z[0]  # Get the first value
    photo_z = photo_z[0]  # Get the first value
    
    # Parse the redshift lists (assuming they are strings of comma-separated values)
    spec_z_list = spec_z.split(", ") if isinstance(spec_z, str) else []
    photo_z_list = photo_z.split(", ") if isinstance(photo_z, str) else []

    # Initialize the best ZSP and ZPH variables
    best_zsp = None
    best_zph = None

    # For Best ZSP (only from spec_z)
    if spec_z_list:
        # Prioritize values in this order: best, zsp, zspec, zs, z
        best_zsp = next((z for z in spec_z_list if 'best' in z.lower()), None)
        if not best_zsp:
            best_zsp = next((z for z in spec_z_list if 'zsp' in z.lower()), None)
        if not best_zsp:
            best_zsp = next((z for z in spec_z_list if 'zspec' in z.lower()), None)
        if not best_zsp:
            best_zsp = next((z for z in spec_z_list if 'zs' in z.lower()), None)
        if not best_zsp:
            best_zsp = next((z for z in spec_z_list if 'z' in z.lower()), None)
        # If none found, pick the first
        if not best_zsp and spec_z_list:
            best_zsp = spec_z_list[0]

    # For Best ZPH (only from photo_z)
    # Prioritize values in this order: best+ml, best, ml, zphot, zpho, zp
    best_zph = next((z for z in photo_z_list if 'best' in z.lower() and 'ml' in z.lower()), None)
    if not best_zph:
        best_zph = next((z for z in photo_z_list if 'best' in z.lower()), None)
    if not best_zph:
        best_zph = next((z for z in photo_z_list if 'ml' in z.lower()), None)
    if not best_zph:
        best_zph = next((z for z in photo_z_list if 'zphot' in z.lower()), None)
    if not best_zph:
        best_zph = next((z for z in photo_z_list if 'zpho' in z.lower()), None)
    if not best_zph:
        best_zph = next((z for z in photo_z_list if 'zp' in z.lower()), None)
    if not best_zph:
        best_zph = next((z for z in photo_z_list if 'z' in z.lower()), None)
    if not best_zph:
        best_zph = next((z for z in photo_z_list if 'z1' in z.lower()), None)
    # If none found, pick the first
    if not best_zph and photo_z_list:
        best_zph = photo_z_list[0]

    # Now, assign them to the DataFrame
    cdf.loc[cdf['ID'] == doi, 'Best ZSP'] = best_zsp
    cdf.loc[cdf['ID'] == doi, 'Best ZPH'] = best_zph

    return cdf




# Update the generate_markdown function to call the assign_best_redshift function
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
        
        if table_count > 1:
            shared_columns = find_shared_columns(content)
            cdf.loc[cdf['ID'] == doi, 'shared_columns'] = ", ".join(shared_columns)

        # Call the function to assign best redshift values for ZSP and ZPH
        cdf = assign_best_redshift(cdf, doi)

    else:
        print(f"Failed to download file. Status code: {response.status_code}")
    
    return cdf



# Read in the Catalogue List
cdf = pd.read_csv('../Catalogue_List_test.csv')

# For each DOI, generate markdown and update the DataFrame
for doi in cdf['ID']:
    generate_markdown(cdf, str(doi).strip())

# After processing all DOIs, save the updated DataFrame back to a new CSV file
cdf.to_csv('../Updated_Catalogue_List.csv', index=False)

print("Updated catalogue list saved successfully!")
