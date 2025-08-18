#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

LESTRADE AUTOWIKI

page.py

v0.2.1

Function for saving markdown page.

@author: joshuaweston

"""

import os

class autowiki:
    
    def __init__(self,doi=None):
        self._content = ""
        self._doi = doi
        self._directory = f"../pages/"
        
        


        for attr in [
            "_best_zsp", "_q_zsp", "_e_zsp",
            "_best_zph", "_q_zph", "_e_zph",
            "_a_best", "_b_best", "_pa_best",
            "_type_labels"
        ]:
            setattr(self, attr, None)


        if doi:
            
            import re
            
            self._doi_tidy  = re.sub(r'[<>:"/\\|?*]', '_', self._doi).strip()
            
            self.get_rm(doi)
            
            self.get_abstract()

            self.get_tables_and_notes()

            self.get_z()

            self.get_best_z()

            self.extract_type_flags()

            self.extract_morphology()

            self.type_flags_md()

            self.set_template()
            
            self.rank()
            
            self._directory = f"../pages/{self._doi_tidy}"
            self._filename = f"{self._doi_tidy}.md"
            
    def get_rm(self,doi):
        
        try:
        
            import requests
                
            url = f"https://cdsarc.cds.unistra.fr/ftp/{doi.strip()}/ReadMe"
                
            response = requests.get(url)
    
            if response.status_code == 200:
                    
                self._readme = response.text
            
            else:
                
                print(response.status_code)
                
                self._readme = None
                
        except Exception as e:
            
            self._readme = e
        
    def set_homepage(self):
        self._content='''
_Lestrade_ is a Python package designed for non-real-time transient-host matching in the Legacy Survey of Space and Time ([LSST](https://rubinobservatory.org/explore/lsst)) Deep Drilling Fields. Designed as a companion to the real-time contextual classification software _Sherlock_, it allows for the downloading, analysis and use of Vizier Deep Drilling Field catalogues in transient science.

Lestrade is divided into two parts. The Lestrade Autowiki provides automated summaries of identified Deep Drilling Field catalogues and their ranked usefulness in transient-host matching, with figures detailing field coverage, redshift distribution and quality among other metrics. Schemas and abstracts for each catalogue are also provided. The Lestrade software allows users to build their own Autowikis with custom data and utilise any combination of this data in a Deep Drilling Field to carry out cross-matching. A machine learning element can assess the confidence of this matching and identify potential catalogue contaminants.

[The Vera C. Rubin Observatory](https://rubinobservatory.org/about) is a brand new astronomical facility on top of Cerro Pachón, a mountain in Northern Chile. Rubin Observatory will conduct a 10-year survey of the Southern Hemisphere sky (referred to as the Legacy Survey of Space and Time, or [LSST](https://rubinobservatory.org/explore/lsst)) with the goal of answering some of astronomers' biggest questions about the Universe.

Every night for a decade, Rubin Observatory will take images of the sky using a 3200 megapixel camera and six different optical filters. Each image covers an area as big as 40 full moons, and the giant 8.4-meter telescope can move between different positions in less than five seconds. In this way, the telescope will image the entire visible sky every 3-4 nights. This makes Rubin Observatory particularly good at detecting objects that have changed in brightness, like supernovae, or in position, like asteroids. Additionally, Rubin Observatory’s light-collecting power and sensitive camera will help us discover ~17 billion stars and ~20 billion galaxies we’ve never seen before.

In addition to the main wide-fast-deep survey (roughly 18,000 deg2), 10-20% of observing time will be dedicated to other programs, including mini-surveys and intensive observation of a set of Deep Drilling Fields. Deeper coverage and more frequent temporal sampling (in at least some of the ugrizy filters) will be obtained for the Deep Drilling Fields than for typical points on the sky. The full Deep Drilling Field program will address a broad range of science topics, including Solar System, Galactic, and extragalactic studies.


***

<img align="right" width="250" src="https://rubinobservatory.org/_next/image?url=https%3A%2F%2FRubin.canto.com%2Fdirect%2Fimage%2F3a4p6ip07138j1p7jt27e4es4t%2F5rWJEW6LnUsKPyEKMsTd080XNGs%2Fm3000%2F800&w=1920&q=75" />
<br/>

### Automated Catalogue Summarisation

- Use the wiki to identify relevant Deep Drilling Field catalogues.

- Construct automated summarisation and analysis of Vizier catalogues for your own wikis. 

- Assess catalogue utility and prioritise data for your science needs.  


<br/>

<img align="left" width="290" src="https://github.com/joshgithubbin/Sherlock-DDF/blob/main/Catalogue%20Plotting/Code/wikipages/images/1246549.png?raw=true" />
<br/>

### Transient-Host Matching

- Match Deep Drilling Field transients to the likeliest host via a morphology-based approach.

- Combine any number of catalogues for a given deep drilling field to carry out offline host matching.

- Assess catalogue usefulness by testing against known transient/galaxy matches.  

<br/>

<img align="right" width="250" src="https://rubinobservatory.org/_next/image?url=https%3A%2F%2FRubin.canto.com%2Fdirect%2Fimage%2F3a4p6ip07138j1p7jt27e4es4t%2F5rWJEW6LnUsKPyEKMsTd080XNGs%2Fm3000%2F800&w=1920&q=75" />
<br/>

### Assess Transient Matches

- Identify high and low-quality matches via a machine learning approach.

- Catch diffraction spikes and identify blended hosts via ML and human-rule techniques.

- Use annotated matches to train error-spotting algorithms.
<br/>
<br/>

***

## Other useful links

More information on Sherlock can be found in [documentation](https://lasair.readthedocs.io/en/develop/core_functions/sherlock.html) for the Lasair Transient Science Platform. 

        '''
        self._directory += "base/"
        
        self._filename = "Home.md"
    
    def set_footer(self):
        self._content = '''
<img align="right" width="300" src="https://blogs.qub.ac.uk/dipsa/wp-content/uploads/sites/14/2022/07/QUB-logo.png" />

**Authors:**

J. G. Weston (QUB) <br/>
D. R. Young (QUB) <br/>
M. Nicholl (QUB) <br/>
S. J. Smartt (Ox, QUB) <br/>
        '''
        self._directory += "base/"
        
        self._filename = "_footer.md"
        
        
    def set_template(self):
    
        self._content = f'''

**Authors:** {self._authors}

## Summary: {self._title}

{self._abstract}

## Coverage \n
 \n
 
![](https://github.com/joshgithubbin/Sherlock-DDF/blob/main/pages/{self._doi_tidy}/im/coverage.png?raw=true)

## Spectroscopic Redshift \n\n

**{self._best_zsp}:** {autowiki.get_explanation(self._best_zsp,self._pd_schema)} \n
\n

<details><summary>See Figure . . .</summary>

![](https://github.com/joshgithubbin/Sherlock-DDF/blob/main/pages/{self._doi_tidy}/im/ZSP.png?raw=true)

</details>

## Photometric Redshift \n\n

**{self._best_zph}:** {autowiki.get_explanation(self._best_zph,self._pd_schema)} \n
\n

<details><summary>See Figure . . .</summary>

![](https://github.com/joshgithubbin/Sherlock-DDF/blob/main/pages/{self._doi_tidy}/im//ZPH.png?raw=true)

</details>

## Morphology \n\n

**{self._a_best}:** {autowiki.get_explanation(self._a_best,self._pd_schema)} \n
**{self._b_best}:** {autowiki.get_explanation(self._b_best,self._pd_schema)} \n
**{self._pa_best}:** {autowiki.get_explanation(self._pa_best,self._pd_schema)} \n
\n

<details><summary>See Figure . . .</summary>

![](https://github.com/joshgithubbin/Sherlock-DDF/blob/main/pages/{self._doi_tidy}/im//morphology.png?raw=true)

</details>
                      
## Type Flags \n\n

{self._type_md}

## Catalogue Schema \n\n

{self._md_tables}
        
        ''' 


    def save(self):
        # Ensure the directory exists
        os.makedirs(self._directory, exist_ok=True)

        # Save the file to that directory
        filepath = os.path.join(self._directory, self._filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(self._content)
            
            
    def get_abstract(self):
        
        import re
        
        if self._readme:
            
            # Extract the title
            title_match = re.search(r"^[^/]+/\S+\s+(\S.*?)(?=\s\(\S+, \d{4}\))", self._readme)
            
            if title_match:
                title = title_match.group(1).strip()
            else:
                title = self._doi
            
            # Step 1: Extract the part of the content containing the abstract
            # Locate the abstract section
            abstract_start = self._readme.find("Abstract:")
            
            if abstract_start == -1:
                 
                cleaned_abstract = "Abstract Section not Found"
                 
                title = self._doi
        
            # Extract content up to the abstract section (including the abstract header)
            header_content = self._readme[:abstract_start].strip()
        
            # Step 2: Find the first and second '===' lines
            # Split the content into lines
            lines = header_content.split('\n')
            
            # Find the index of the first and second '===' lines
            first_equals_index = None
            second_equals_index = None
        
            for i, line in enumerate(lines):
                if line.startswith('==='):
                    if first_equals_index is None:
                        first_equals_index = i
                    elif second_equals_index is None:
                        second_equals_index = i
                        break  # No need to look further
        
            if first_equals_index is not None and second_equals_index is not None:
                # Extract everything between the first and second '===' lines
                author_list = "\n".join(lines[first_equals_index + 1:second_equals_index]).strip()
                # Clean up extra spaces, line breaks, and commas
                author_list = re.sub(r"\n", ", ", author_list)  # Join multi-line authors into one line
                author_list = re.sub(r"\s{2,}", " ", author_list)  # Remove extra spaces between names
            else:
                author_list = "Authors not found."
        
            # Step 3: Find the second occurrence of '.,' and remove everything before it
            # Match the second occurrence of ".,"
            first_period_comma = author_list.find(".,")
            second_period_comma = author_list.find(".,", first_period_comma + 2)  # Find second occurrence
        
            if second_period_comma != -1:
                # Start the author list from the character after the second ".,"
                author_list = author_list[second_period_comma + 2:].strip()
            else:
                author_list = "Authors list format error."
        
            # Step 4: Extract the abstract text
            # The abstract ends before we hit the next capitalized line (e.g., "Description:" or similar)
            abstract_match = re.search(
                r"(?<=Abstract:\n)(.*?)(?=\n[A-Z][^\n]{5,})",  # Match the abstract part
                self._readme,
                re.DOTALL
            )
        
            if abstract_match:
                raw_abstract = abstract_match.group(1)
                cleaned_abstract = re.sub(r"\n\s+", " ", raw_abstract)  # Join lines
                cleaned_abstract = re.sub(r" {2,}", " ", cleaned_abstract)  # Remove extra spaces
                cleaned_abstract = cleaned_abstract.strip()
            else:
                cleaned_abstract = "Abstract section not found."
                
                
            self._abstract = cleaned_abstract
            self._authors = author_list
            self._title = title

        
    def get_tables_and_notes(self):
        
        import re
        import pandas as pd
        
        # Extract each 'Byte-by-byte Description of file:' block
        table_matches = re.findall(
            r"(Byte-by-byte Description of file: [^\n]+(?:\n.*?)+?)\n{2,}",
            self._readme,
            re.DOTALL
        )
    
        markdown_tables = []
        all_dfs = []
    
        if not table_matches:
            print("No tables found in the document.")
            return ""
    
        for idx, table_data in enumerate(table_matches, start=1):
            # Remove long dashed separators
            table_data = re.sub(r"-{50,}", "", table_data)
    
            # Extract the table name
            table_name_match = re.search(r"file:\s*(\S+)", table_data)
            table_name = table_name_match.group(1) if table_name_match else f"table{idx}.dat"
    
            # Extract notes (including multi-line)
            note_match = re.search(r"Note\s*\(\d+\):\s*(.*?)(?=\n-{3,}|\n*$)", table_data, re.DOTALL)
            note_text = note_match.group(1).strip() if note_match else None
    
            # Parse the table into a DataFrame with continuation line support
            table_df = autowiki.parse_table_block(table_data)
    
            # Convert DataFrame to Markdown and wrap in collapsible section
            markdown_table = f"<details>\n<summary>{table_name} catalogue schema</summary>\n\n"
            markdown_table += table_df.to_markdown(index=False)
    
            if note_text:
                markdown_table += f"\n\n**Note**: {note_text}\n"
    
            markdown_table += "\n</details>\n"
            markdown_tables.append(markdown_table)
            
            all_dfs.append(table_df)
    
        self._md_tables =  "\n".join(markdown_tables)
        self._pd_tables = all_dfs
        self._pd_schema = pd.concat(self._pd_tables)
        
    def get_z(self):
        
        import re
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
        abstract_match = re.search(r"Abstract:\s*(.*?)\n{2,}", self._readme, re.DOTALL)
        abstract = abstract_match.group(1) if abstract_match else ""

        # Extract table sections
        table_matches = re.findall(
            r"(Byte-by-byte Description of file: [^\n]+(?:\n.*?)+?)\n{2,}",
            self._readme,
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
        self._zsp = list(set(spectroscopic_redshift_labels))
        self._zph = list(set(photometric_redshift_labels))
        self._qz = list(set(redshift_qualities_labels))
        self._oz = list(set(other_redshift_metrics_labels))

    def get_best_z(self):
        
        if self._zsp:

            # Prioritize values in this order: best, zsp, zspec, zs, z
            self._best_zsp = next((z for z in self._zsp if 'best' in z.lower()), None)
            if not self._best_zsp:
                self._best_zsp = next((z for z in self._zsp if 'zsp' in z.lower()), None)
            if not self._best_zsp:
                self._best_zsp = next((z for z in self._zsp if 'zspec' in z.lower()), None)
            if not self._best_zsp:
                self._best_zsp = next((z for z in self._zsp if 'zs' in z.lower()), None)
            if not self._best_zsp:
                self._best_zsp = next((z for z in self._zsp if 'z' in z.lower()), None)
            # If none found, pick the first
            if not self._best_zsp and self._zsp:
                self._best_zsp = self._zsp[0]
                
        else:
            self._best_zsp = None
        
               
        # For Best ZPH (only from photo_z)
        
        if self._zph:
            # Prioritize values in this order: best+ml, best, ml, zphot, zpho, zp
            self._best_zph = next((z for z in self._zph if 'best' in z.lower() and 'ml' in z.lower()), None)
            if not self._best_zph:
                self._best_zph = next((z for z in self._zph if 'best' in z.lower()), None)
            if not self._best_zph:
                self._best_zph = next((z for z in self._zph if 'ml' in z.lower()), None)
            if not self._best_zph:
                self._best_zph = next((z for z in self._zph if 'zphot' in z.lower()), None)
            if not self._best_zph:
                self._best_zph = next((z for z in self._zph if 'zpho' in z.lower()), None)
            if not self._best_zph:
                self._best_zph = next((z for z in self._zph if 'zp' in z.lower()), None)
            if not self._best_zph:
                self._best_zph = next((z for z in self._zph if 'z' in z.lower()), None)
            if not self._best_zph:
                self._best_zph = next((z for z in self._zph if 'z1' in z.lower()), None)
            # If none found, pick the first
            if not self._best_zph and self._zph:
                self._best_zph = self._zph[0]
                
        else:
            
            self._best_zph = None
                
        #do quality/errors exist?
        
        if self._qz:
            
            if self._best_zsp:
                
                if f"q_{self._best_zsp}" in self._qz:
                    
                    self._q_zsp = f"q_{self._best_zsp}"
                    
                if f"e_{self._best_zsp}" in self._qz:
                    
                    self._e_zsp = f"e_{self._best_zsp}"
            if self._best_zph:
                if f"q_{self._best_zph}" in self._qz:
                        
                    self._q_zph = f"q_{self._best_zph}"
                        
                if f"e_{self._best_zph}" in self._qz:
                        
                    self._e_zph = f"e_{self._best_zph}"
                    

    def extract_morphology(self):
        
        import pandas as pd
        
        table_df = pd.concat(self._pd_tables)
        
        amajor_key = ['a_imag', 'semi-major', 'major']
        bmajor_key = ['b_imag', 'semi-minor', 'minor']
        pa_key = ['pa', 'theta', 'position angle']
        axis_units = ['deg', 'pix', 'rad', 'arcsec', 'arcmin']

        table_df['Units'] = table_df['Units'].fillna("").str.strip().str.lower()

        def match_labels(keywords):
            matches = []
            for _, row in table_df.iterrows():
                explanation = str(row['Explanations']).lower()
                unit = str(row['Units']).lower()
                if unit in axis_units and any(keyword in explanation for keyword in keywords):
                    matches.append(row['Label'])
            return list(set(matches))

        def filter_out_unwanted(labels, unwanted_substrings):
            return [label for label in labels if not any(uw in label.lower() for uw in unwanted_substrings)]

        def rank_labels(labels, priority_order):
            labels = list(set(labels))
        
            def label_priority(lbl):
                l = lbl.lower()
                # Exact match with priority list
                for i, p in enumerate(priority_order):
                    if l == p:
                        return (0, i)
                # Startswith match but not exact
                for i, p in enumerate(priority_order):
                    if l.startswith(p) and l != p:
                        return (1, i)
                # Fallback
                return (2, l)
        
            return sorted(labels, key=label_priority)


        # Matching and filtering
        a_matches = filter_out_unwanted(match_labels(amajor_key), ['pa', 'area', 'angle', 'e_'])
        b_matches = filter_out_unwanted(match_labels(bmajor_key), ['pa', 'area', 'angle', 'e_'])
        pa_matches = filter_out_unwanted(match_labels(pa_key), ['e_', 'par'])

        # Ranking
        a_priority = ['a', 'amaj', 'a1', 'a2']
        b_priority = ['b', 'bmin', 'b1', 'b2']
        pa_priority = ['pa', 'theta', 'pa1', 'pa2','paw']

        self._a_ranked = rank_labels(a_matches, a_priority)
        self._b_ranked = rank_labels(b_matches, b_priority)
        self._pa_ranked = rank_labels(pa_matches, pa_priority)
        
        if self._a_ranked:
            self._a_best = self._a_ranked[0]
        else:
            self._a_best = None
        if self._b_ranked:
            self._b_best = self._b_ranked[0]
        else:
            self._b_best = None
        if self._pa_ranked:
            self._pa_best = self._pa_ranked[0]  
        else:
            self._pa_best = None            
    
    def extract_type_flags(self):
        
        import re
        
        # Exact match keywords (case-insensitive)
        exact_keywords = ['AGN', 'S/G', 'G/S']

        # Substring match keywords (case-insensitive)
        substring_keywords = ['type', 'class']

        self._type_labels = []

        # Extract table sections
        table_matches = re.findall(
            r"(Byte-by-byte Description of file: [^\n]+(?:\n.*?)+?)\n{2,}",
            self._readme,
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
                        self._type_labels.append(label)

                    # Check substring matches
                    elif any(kw in label.lower() for kw in substring_keywords):
                        self._type_labels.append(label)
                        
        self._type_labels = list(dict.fromkeys(self._type_labels))
    
    def type_flags_md(self):
        
        type_md = ''
        
        for i in self._type_labels:
            
            type_md += f"**{i}:** {autowiki.get_explanation(i,self._pd_schema)}\n\n"
            
        self._type_md = type_md
    
    def rank(self):
        
        if self._best_zsp:
            
            self._lrank = 'A'
            
        elif self._best_zph:
            
            self._lrank = 'B'
            
        else:
            
            self._lrank = 'C'
            
        if self._a_best and self._b_best and self._pa_best and self._type_labels:
            
            self._lrank += '+'
        
        elif not self._a_best and not self._b_best and not self._pa_best and not self._type_labels:
            
            self._lrank += '-'
        
    
    
    @staticmethod
    def get_explanation(label,df):
        
        matches = df.loc[df['Label'] == label, 'Explanations']
        explanation = matches.iloc[0] if not matches.empty else None
        
        return explanation


    @staticmethod
    def parse_table_block(table_data):
        
        import re
        import pandas as pd
        
        rows = []
        current_row = None
    
        lines = table_data.splitlines()
    
        for line in lines:
            line = line.rstrip()
    
            # Skip headers, separators, and empty lines
            if not line.strip() or re.match(r"^\s*-{3,}\s*$", line) or re.match(r"^\s*Bytes\s+Format", line):
                continue
    
            # Match row start: Byte range + Format + Units + Label + Explanation
            match = re.match(
                r"^\s*(\d+(?:-\s*\d+)?)\s+(\S+)\s+(\S+)\s+(\S+)\s+(.*)", line
            )
    
            if match:
                if current_row:
                    rows.append(current_row)
                current_row = list(match.groups())
            elif current_row:
                # Continuation line → add to current explanation
                continuation = line.strip()
                current_row[-1] += " " + continuation
    
        if current_row:
            rows.append(current_row)
    
        if not rows:
            print("[parse_table_block] No rows parsed from block.")
            print("[DEBUG] Block preview:")
            print("\n".join(lines[:15]))
            
    
        return pd.DataFrame(rows, columns=["Bytes", "Format", "Units", "Label", "Explanations"])
    
    
    
class sidebar:
    
    def __init__(self, key):
        
        self._content = ""
        self._directory = f"../pages/base/"
        self._filename ="_sidebar.md"
        
        self._key = key
        
        
        self.set_all_grades()
        self.set_template()
        
    def set_template(self):
        
        self._content = f'''
        
![](https://github.com/joshgithubbin/Sherlock-DDF/blob/main/pages/base/im/lestrade.png?raw=true)

### [Home](https://github.com/joshgithubbin/Sherlock-DDF/wiki)

### Help

- [Catalogue Ranking System](https://github.com/joshgithubbin/Sherlock-DDF/wiki/Catalogue-Ranking-System)

- [Cross-Matching Methodology](https://github.com/joshgithubbin/Sherlock-DDF/wiki/Cross-Matching-Methodology)

- [Lestrade User Guide](https://github.com/joshgithubbin/Sherlock-DDF/wiki/Lestrade-User-Guide)


***


![](https://github.com/joshgithubbin/Sherlock-DDF/blob/main/pages/base/im//autowiki.png?raw=true)

### Catalogues:

<details><summary>A+</summary>

{self._A_plus_md}

</details>

<details><summary>A</summary>

{self._A_md}

</details>

<details><summary>A-</summary>

{self._A_minus_md}

</details>

<details><summary>B+</summary>

{self._B_plus_md}

</details>

<details><summary>B</summary>

{self._B_md}

</details>

<details><summary>B-</summary>

{self._B_minus_md}

</details>

<details><summary>C+</summary>

{self._C_plus_md}

</details>

<details><summary>C</summary>

{self._C_md}

</details>

<details><summary>C-</summary>

{self._C_minus_md}

</details>
'''
    
    def set_grade_md(self, grade):
        
        elements = [i for i in self._key if i[1] == grade]
        md = ''.join(f'- [{i[2]}](https://github.com/joshgithubbin/Sherlock-DDF/wiki/{i[0]})\n\n' for i in elements)
        
        if grade == 'A+':
            self._A_plus_md = md
        elif grade == 'A':
            self._A_md = md
        elif grade == 'A-':
            self._A_minus_md = md
            
        if grade == 'B+':
            self._B_plus_md = md
        elif grade == 'B':
            self._B_md = md
        elif grade == 'B-':
            self._B_minus_md = md 
            
        if grade == 'C+':
            self._C_plus_md = md
        elif grade == 'C':
            self._C_md = md
        elif grade == 'C-':
            self._C_minus_md = md
            
            
    def set_all_grades(self):
        
        for q in ['A+','A','A-','B+','B','B-','C+','C','C-']:
        
            self.set_grade_md(q)
            
    def save(self):
        # Ensure the directory exists
        os.makedirs(self._directory, exist_ok=True)

        # Save the file to that directory
        filepath = os.path.join(self._directory, self._filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(self._content)        
