[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/29xHZNvH)
# COMP100 2024F Problem Set 3:

## Deadline: December 16, 2024 23.59 

The test cases given are just sample tests, and additional test cases may be used while grading.

# Winter is Coming: Preparing for the Great War (100 Points)

The Wall, the northern defense of the Seven Kingdoms, is under threat from an army of White Walkers. Each of the Night's Watch gates is manned by soldiers from various noble houses, who must defend their assigned doors. However, the enemy is overwhelming, and reinforcements may be needed. The realm’s strategy is now in the hands of the students, who must simulate troop allocation and resource management in a way that ensures the survival of the Wall.

Your mission is to handle the data of White Walkers, stationed soldiers, and available resources. Through a sequence of tasks, you will decrypt classified information, assess defense capabilities, and manage reinforcements to strengthen the Wall. Lastly, you will encrypt the final output to archive it in Kingsland’s secure records.

**NOTE**: You should write your all output files for all parts into a folder named `solution_outputs` for test codes to work correctly. 

## Part A: Breaking the Seal

All critical information related to the defense of the Wall is sealed with a magical spell to ensure secrecy. Your first task is to create a global decryption function capable of unlocking this information. This function will be used throughout the problem set to decrypt various files. You should write a `function decrypt_the_message(file, s, output_path)` that takes input file path, shift (integer s), and output file path.

Task:

- Implement a decryption function based on a Caesar cipher with a shift of -3.

- Use this function to decrypt all input files provided in this problem set.

- Ensure that the same decryption logic can be applied to any encrypted file used in subsequent steps.

Method:

- You should apply a Caesar cipher with a shift of -3 to uppercase characters, lowercase characters and numericals seperately.
- For numericals, you should shift each digit in a 0-9 circular motion (e.g if encrypted value is 9 then decrypted is 6 or if encrypted value is 2 then decrypted is 9)
- Any characters other than alphanumerical should stay as they are.

Example:
If the encrypted content is:
`Hdvwzdwfk eb wkh Vhd,Hbulh,573,683`

After applying the decryption function with the key (e.g., a shift of -3), the output should be:

`Eastwatch by the Sea,Eyrie,240,350`

## Part B: Aggregating House Contributions

Once the encrypted file is decrypted, process the possible contributions of the noble houses by combining their resources into a unified structure.

Input File:

You will be given an encrypted file, `encrypted_houses.txt`, containing rows in the following format:

```python
Vwdun,93,4213
Odqqlvwhu,1773,6823
Edudwkhrq,1963,8903
```

After decryption, the file will contain data in this format:
```python
Stark,60,1980
Lannister,8440,3590
Baratheon,8630,5670
```

Output File:

Create a file named `aggregated_houses.txt`, containing the aggregated contributions of each unique house in the following format:

```python
Stark: {'soldiers': 110, 'weapons': 6670}
Lannister: {'soldiers': 49960, 'weapons': 32560}
Baratheon: {'soldiers': 14390, 'weapons': 7650}
Targaryen: {'soldiers': 6000, 'weapons': 3000}
```

Requirements:

- Use the global decryption function to decrypt encrypted_houses.txt.

- Parse each row and store the data in a dictionary where:

- The keys are the house names.

- The values are dictionaries containing soldiers and weapons.

- If a house appears multiple times, sum up their soldiers and weapons.

Write the resulting dictionary into `aggregated_houses.txt`.

## Part C: Decoding House Assignments

Jon Snow’s strategy depends on knowing the assignments of houses and their stationed forces at each of the gates along the Wall. This information is encrypted for security reasons.

Input File:

You will receive an encrypted file named `encrypted_assignments.txt`. Each row in the file contains an encrypted string specifying:

- Which house is responsible for a particular gate.

- The number of soldiers and weapons stationed there.

Example (encrypted content):
```python
Hdvwzdwfk eb wkh Vhd,Hbulh,573,683
Fdvwoh Eodfn,Wdujdubhq,513,4353
Vkdgrz Wrzhu,Wxoob,423,513
```

After decryption, the content should look like this:
```python
Eastwatch by the Sea,Eyrie,240,350
Castle Black,Targaryen,280,1020
Shadow Tower,Tully,190,280
```

Create a file named `assignments_decrypted.txt` with the following format:
```python
Eastwatch by the Sea,Eyrie,240,350
Castle Black,Targaryen,280,1020
Shadow Tower,Tully,190,280
```

Now you should update the assignments by sending all troops and weapons possible from the house that is responsible of the gate. You should use both `assignments_decrypted.txt` and `aggregated_houses.txt` from previous part to decide how many soldiers will be sent to which gate by whom and update both files.

Once the houses have stationed their forces at the gates, their contributions in `aggregated_houses.txt` must be updated to reflect that they can no longer provide additional support. Add the soldiers and weapons from that house to gates and set their values to 0. Write you new houses dict to `updated_houses.txt` and your new gate assignments to `updated_assignments.txt` in the form:

- `updated_houses.txt`:
```python
Stark: {'soldiers': 110, 'weapons': 6670}
Lannister: {'soldiers': 49960, 'weapons': 32560}
Baratheon: {'soldiers': 14390, 'weapons': 7650}
Targaryen: {'soldiers': 0, 'weapons': 0}
```
- `updated_assignments.txt`:
```python
Eastwatch by the Sea: {'house': 'Eyrie', 'soldiers': 3240, 'weapons': 1850}
Castle Black: {'house': 'Targaryen', 'soldiers': 6280, 'weapons': 4020}
Shadow Tower: {'house': 'Tully', 'soldiers': 5190, 'weapons': 2280}
```

## Part D: White Walker Threat Analysis and Reinforcements

The Wall's defense relies on precise allocation of soldiers and weapons. For each gate, reinforcements must be provided by houses that match the **exact** required number of soldiers and weapons. This task is divided into two parts:

1. **D.1 Soldiers:** Allocate the exact number of soldiers required for each gate and update all records.
2. **D.2 Weapons:** Allocate the exact number of weapons required for each gate after soldiers are assigned and update all records.

Both steps involve updating house resources (`updated_houses.txt`) and gate assignments (`updated_assignments.txt`).

### **Inputs for Step D**

1. **White Walker Threat Levels:**
   A dictionary specifying the number of White Walkers at each gate.

2. **Files:**
   - `updated_houses.txt`: Contains aggregated resources for all houses.
   - `updated_assignments.txt`: Lists stationed forces at each gate.

Refer to the example part bellow for usage and updates to these files.

### **D.1 Soldiers: Allocating Reinforcements**

#### Objective:
Allocate soldiers for each gate by finding houses with **exactly** the required number of soldiers.

#### Steps:
1. **Calculate Required Soldiers**  
   For each gate:
   $$
   \text{Required Soldiers} = \text{White Walkers at Gate} - \text{Stationed Soldiers}
   $$

2. **Find Matching Houses**  
   - Use binary search to find a house in `updated_houses.txt` with exactly the required number of soldiers.

3. **Update Records**  
   - Update the `updated_assignments.txt` file to reflect the new total number of soldiers at the gate.
   - Deduct the allocated soldiers from the matching house in `updated_houses.txt`.

### **D.2 Weapons: Allocating Reinforcements**

#### Objective:
Allocate weapons for each gate by finding houses with **exactly** the required number of weapons.

#### Steps:
1. **Calculate Required Weapons**  
   For each gate:
   $$
   \text{Required Weapons} = \text{White Walkers at Gate} - \text{Initial Number of Weapons}
   $$

2. **Find Matching Houses**  
   - Use binary search to find a house in `updated_houses.txt` with exactly the required number of weapons.

3. **Update Records**  
   - Update the `updated_assignments.txt` file to reflect the new total number of weapons at the gate.
   - Deduct the allocated weapons from the matching house in `updated_houses.txt`.

### Binary Search: Core Algorithm for Matching Reinforcements

Binary search is an efficient algorithm for finding a specific value in a **sorted dataset**. It works by repeatedly dividing the search range in half, significantly reducing the number of comparisons needed to locate the target value.

#### **How Binary Search Works**

1. **Sort the Data**:  
   Ensure the dataset is sorted in ascending order.

2. **Initialize Search Range**:  
   Define the range with a starting point (`low`) and an ending point (`high`).

3. **Find the Middle Element**:  
   Calculate the midpoint:  
   
   $$\text{mid} = \frac{\text{low} + \text{high}}{2}$$

4. **Compare the Target with the Middle Element**:  
   - If they match, the search is complete.  
   - If the middle element is smaller than the target, adjust the range to the upper half (`low = mid + 1`).  
   - If it’s larger, adjust to the lower half (`high = mid - 1`).

5. **Repeat Until Found or Exhausted**:  
   Continue until the target is located or the range is empty.

#### **Binary Search in Dictionaries**

1. **Sort by Key of Interest**:  
   For dictionaries, sort entries based on the target key (e.g., `'soldiers'` or `'weapons'`).

2. **Apply Binary Search**:  
   Perform binary search on the sorted dictionary keys, referencing the values during comparisons.

3. **Find and Retrieve**:  
   Once a match is located, access the full dictionary entry for the corresponding key.

### Additional Resources

- **Animations**: [Binary Search Visualization](https://yongdanielliang.github.io/animation/web/BinarySearchNew.html)  
- **Videos**: [Binary Search Explained and Implemented](https://www.youtube.com/watch?v=DnvWAd-RGhk)  

### Visualization

![Binary Search Visualization](/sources/bs.gif)

This visual demonstrates the difference between binary search and sequential search, highlighting how binary search efficiently narrows down the search range to locate the target.

### Example:

#### Inputs:
```python
white_walkers = {
    "Eastwatch by the Sea": 300,
    "Castle Black": 500,
    "Shadow Tower": 200
}

decrypted_assignments = {
    'Eastwatch by the Sea': {'house': 'Stark', 'soldiers': 200, 'weapons': 100},
    'Castle Black': {'house': 'Targaryen', 'soldiers': 150, 'weapons': 250},
    'Shadow Tower': {'house': 'Greyjoy', 'soldiers': 180, 'weapons': 280}
}

aggregated_houses = {
    'Stark': {'soldiers': 0, 'weapons': 0},
    'Targaryen': {'soldiers': 0, 'weapons': 0},
    'Greyjoy': {'soldiers': 0, 'weapons': 0},
    'Lannister': {'soldiers': 100, 'weapons': 250},
    'Baratheon': {'soldiers': 20, 'weapons': 200},
    'Martell': {'soldiers': 350, 'weapons': 350}
}
```

### **D.1 Soldiers:**
1. **'Eastwatch by the Sea'**  
   - Required Soldiers: \( 300 - 200 = 100 \)  
   - Match: Lannister (100 soldiers).  
   - Update:
     - **`updated_assignments.txt`**: Update 'Eastwatch by the Sea' soldiers to 300.
     - **`updated_houses.txt`**: Update Lannister soldiers to:
       ```python
       'Lannister': {'soldiers': 0, 'weapons': 100}
       ```

2. **'Castle Black'**  
   - Required Soldiers: \( 500 - 150 = 350 \)  
   - Match: Martell (350 soldiers).  
   - Update:
     - **`updated_assignments.txt`**: Update 'Castle Black' soldiers to 500.
     - **`updated_houses.txt`**: Update Martell soldiers to:
       ```python
       'Martell': {'soldiers': 0, 'weapons': 350}
       ```

3. **'Shadow Tower'**  
   - Required Soldiers: \( 200 - 180 = 20 \)  
   - Match: Baratheon (20 soldiers).  
   - Update:
     - **`updated_assignments.txt`**: Update 'Shadow Tower' soldiers to 200.
     - **`updated_houses.txt`**: Update Baratheon soldiers to:
       ```python
       'Baratheon': {'soldiers': 0, 'weapons': 200}
       ```

### **D.2 Weapons:**
1. **'Eastwatch by the Sea'**  
   - Required Weapons: \( 300 - 100 = 200 \)  
   - Match: Baratheon (200 weapons).  
   - Update:
     - **`updated_assignments.txt`**: Update 'Eastwatch by the Sea' weapons to 300.
     - **`updated_houses.txt`**: Update Baratheon weapons to:
       ```python
       'Baratheon': {'soldiers': 0, 'weapons': 0}
       ```

2. **'Castle Black'**  
   - Required Weapons: \( 500 - 250 = 250 \)  
   - Match: Lannister (250 weapons).  
   - Update:
     - **`updated_assignments.txt`**: Update 'Castle Black' weapons to 500.
     - **`updated_houses.txt`**: Update Lannister weapons to:
       ```python
       'Lannister': {'soldiers': 0, 'weapons': 0}
       ```

3. **'Shadow Tower'**  
   - Required Weapons: \( 200 - 280 = -80 \)  
   - No weapons needed; no updates required.

### Outputs:

1. **Updated `final_assignments.txt`:**
```python
{
    'Eastwatch by the Sea': {'house': 'Stark', 'soldiers': 300, 'weapons': 300},
    'Castle Black': {'house': 'Targaryen', 'soldiers': 500, 'weapons': 500},
    'Shadow Tower': {'house': 'Greyjoy', 'soldiers': 200, 'weapons': 280}
}
```

2. **Updated `final_houses.txt`:**
```python
{
    'Stark': {'soldiers': 0, 'weapons': 0},
    'Targaryen': {'soldiers': 0, 'weapons': 0},
    'Greyjoy': {'soldiers': 0, 'weapons': 0},
    'Lannister': {'soldiers': 0, 'weapons': 0},
    'Baratheon': {'soldiers': 0, 'weapons': 0},
    'Martell': {'soldiers': 0, 'weapons': 350}
}
```
1. **Final Assignment File**:  
   **`solution_outputs/final_assignment.txt`**  
   Contains updated reinforcements for each gate (soldiers and weapons) after allocation.

2. **Final Houses File**:  
   **`solution_outputs/final_houses.txt`**  
   Contains updated house resources reflecting deductions after reinforcements.

### Additional Notes:

1. **Guaranteed Reinforcements**:
   - Every gate will receive reinforcements if a matching house is available. Test data ensures that exact matches are always provided for soldiers and weapons to avoid allocation failures.

2. **Edge Case Explanation**:
   - For the **Shadow Tower** case in **4.b Weapons**, no additional weapons were required because the initial number of weapons at the gate already exceeded the total requirement. Therefore, no updates were made to `updated_houses.txt` or `updated_assignments.txt` for weapons in this case.

## Part E: Final Encryption of Results

- Once all tasks are complete, encrypt the final output using the same key and logic as the decryption function.

- Encrypt and save the final updated data into `solution_outputs` folder with files named `encrypted_final_assignments.txt` and `encrypted_final_houses.txt`.

## Deliverables and Workflow Summary

#### Part A: Decrypt Files
- **Input**: `encrypted_houses.txt`, `encrypted_assignments.txt`  
- **Output**: `houses_decrypted.txt`, `assignments_decrypted.txt`  
- **Action**: Decrypt files using a Caesar cipher with shift -3.

#### Part B: Aggregate House Contributions
- **Input**: `houses_decrypted.txt`  
- **Output**: `aggregated_houses.txt`  
- **Action**: Combine soldier and weapon data for each house.

#### Part C: Update Assignments
- **Input**: `assignments_decrypted.txt`, `aggregated_houses.txt`  
- **Output**: `updated_houses.txt`, `updated_assignments.txt`  
- **Action**: Assign available resources to gates and update records.

#### Part D: Allocate Reinforcements
- **Input**: `updated_houses.txt`, `updated_assignments.txt`, White Walker threat levels  
- **Output**: `final_houses.txt`, `final_assignments.txt`  
- **Action**: Allocate exact resources to gates using binary search and update files.

#### Part E: Encrypt Final Results
- **Input**: `final_houses.txt`, `final_assignments.txt`  
- **Output**: `encrypted_final_houses.txt`, `encrypted_final_assignments.txt`  
- **Action**: Encrypt the final results using Caesar cipher with shift 3.

### Files in `solution_outputs` Folder

1. **Decrypted Files**:  
   - `houses_decrypted.txt`  
   - `assignments_decrypted.txt`

2. **Processed Files**:  
   - `aggregated_houses.txt`  
   - `updated_houses.txt`  
   - `updated_assignments.txt`

3. **Final Files**:  
   - `final_houses.txt`  
   - `final_assignments.txt`

4. **Encrypted Files**:  
   - `encrypted_final_houses.txt`  
   - `encrypted_final_assignments.txt`
