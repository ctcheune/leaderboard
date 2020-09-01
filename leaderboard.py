import pandas as pd

def getStudentList():
    '''Prompts user for csv file of students names
       and creates a blank scoreboard

       Returns:

            stud_df (dataframe) : 
    '''

    #get input from user
    #stud_data = input("Please enter a csv file containing the names of the students in the first column\n")
    
    #TODO: if it's not a csv, ask again
    #TODO: if other cols have input, ask again
    
    #Get all student names and put in a column of df
    stud_data = pd.read_csv("C:/Users/Admin/Desktop/Summer Projects/test_names.csv")
    names_lists = stud_data.values.tolist()
    names = []

    for name in names_lists:
        for n in name:
            names.append(n)

    #Get number of student names = num_studs
    num_studs = len(names)
    
    stud_df = pd.DataFrame({'Rank': ['-'] * num_studs,
                            'Name': names,
                            'Score': [0] * num_studs
                           })
    print(stud_df)
    return(stud_df)


def updateScore(winner):

    for name in df['Name']:
        if (winner == name):
            df.loc[df['Name'] == winner, 'Score'] += 1

    updateRank()

def updateRank():
    df.sort_values(by = 'Score', ascending = False, inplace=True)
    df["Rank"] = df["Score"].rank(method = 'dense', ascending = False)

    print (df)

#get this input from user

df = getStudentList()

#"main"
updateScore("Serena Williams")
updateScore("Serena Williams")
updateScore("Serena Williams")
updateScore("Selena Morales")
updateScore("Aminata Dialo")
updateScore("Aminata Dialo")
updateScore("Aminata Dialo")
updateScore("Aminata Dialo")
updateScore("Aminata Dialo")
updateScore("Selena Morales")
updateScore("Selena Morales")





    
    