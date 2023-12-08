
# Ombudsman System

This project is an examination for university where I am challenged to create an Ombudsman System using Python "basic".


## Functionalities

- List complaints
The system should check if the list of complaints is empty. If it is, the following message should be displayed: 'No complaints registered in the system.' On the other hand, if there are complaints, they should be presented in the following format:
1) Restroom without paper
2) Toilet flush not working
3) Air conditioning not functioning (true!)
- Add new complaint
The system should request the title of the new complaint and add it to the list. Finally, confirm with the following message: 'Complaint successfully registered. The complaint code is 1.' Note that '1' corresponds to the complaint code. For example, the first complaint (in memory, with index 0) will have code 1, and the second complaint (in memory, with code 1) will have code 2, and so on
- Remove a complaint
The system should initially display all existing complaints in the system, similar to Option 1. Afterward, the user should be prompted to enter the code of the complaint they wish to remove. Subsequently, the system should remove the complaint from the list.

Additionally, the system should validate whether the provided removal code is valid. For instance, codes such as -1, 0, and other non-positive numbers are not valid. In such cases, the system should display: 'Invalid code.
- Search for a complaint by code
The system should prompt the user to enter the code of the complaint they wish to research. Once provided, the title of the complaint is displayed.

Additionally, the system should validate whether the provided code for research is valid. For example, codes such as -1, 0, and other non-positive numbers are not valid. In such cases, the system should display: 'Invalid code.
- Exit


## Author

- [@gomes.svg](https://www.instagram.com/gomes.svg/)

