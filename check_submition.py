# Do pip install gitpython
# run with python check_submition.py hw-id.txt
import os
import sys
import subprocess
import re
import git
global commit, id, giturl, grade, total


def main():
    print("8 Test(1,2,3,4,5,6,7,8)\n")
    total = 8
    grade = 0
    try:
        hw = open(sys.argv[1], 'r+').read().splitlines()
        repo_url = hw[0]
        commit_id = hw[1]
        repo_path = hw[2]
        if(os.path.exists(repo_path)):
            return print("Directory  " + repo_path+" is already exists, so please delete it and run the command again")
        print(repo_path)
        repo = git.Repo.clone_from(repo_url, repo_path, no_checkout=True)
        repo.git.checkout(commit_id)
        # base dirs
        os.mkdir(repo_path+'/inputs')
        os.mkdir(repo_path+'/outputs')
        basedir = os.getcwd().replace("\\", "/")+"/"+repo_path+"/"
    except Exception as e:
        print(e)
    try:
# test 1
        print("\nTest 1 (print(q.XtimesY(-2,2)=0.0 no setting)")
        f = open(basedir+"/inputs/test1.py", 'w+')
        f.write("import sys")
        f.write("\n")
        f.write("sys.path.insert(1,'"+basedir+"')")
        f.write("\n")
        f.write("import equations as q")
        f.write("\n")
        f.write("print(q.XtimesY(-2,2))")
        f.close()
        command = "cd "+repo_path+" && python " + basedir + \
            "/inputs/test1.py" + " > "+basedir+"/outputs/test1.txt"
        proc = subprocess.Popen(command, shell=True)
        proc.wait()
        f = open(basedir+"/outputs/test1.txt", 'r+').read().splitlines()
        passed = "False"
        temp = 0
        for x in f:
            if float(x)==0.0:
                temp += 1
        if temp == 1:
            passed = "True"
            grade+=1
        print(passed)

        f = open(basedir+"/outputs/Total.txt", 'a')
        f.write("\nTest1:"+passed)
        f.close()
    except Exception as e:
        print(e)
# test 2
    try:
        print("\nTest 2 (print(q.XtimesY(-2.2,-2)=0.0 - no setting for)")
        f = open(basedir+"/inputs/test2.py", 'w+')
        f.write("import sys")
        f.write("\n")
        f.write("sys.path.insert(1,'"+basedir+"')")
        f.write("\n")
        f.write("import equations as q")
        f.write("\n")
        f.write("print(q.XtimesY(-2.2,-2))")
        f.close()
        command = "cd "+repo_path+" && python " + basedir + \
            "/inputs/test2.py" + " > "+basedir+"/outputs/test2.txt"
        proc = subprocess.Popen(command, shell=True)
        proc.wait()
        f = open(basedir+"/outputs/test2.txt", 'r+').read().splitlines()
        passed = "False"
        temp = 0
        for x in f:
            if float(x)==0.0:
                temp += 1
        if temp == 1:
            passed = "True"
            grade+=1
        print(passed)
        f = open(basedir+"/outputs/Total.txt", 'a')
        f.write("\nTest2:"+passed)
        f.close()
    except Exception as e:
        print(e)
#test 3
    try:
        print("\nTest 3 (print(q.sqrt(2.5,4)=1.741)")
        f = open(basedir+"/inputs/test3.py", 'w+')
        f.write("import sys")
        f.write("\n")
        f.write("sys.path.insert(1,'"+basedir+"')")
        f.write("\n")
        f.write("import equations as q")
        f.write("\n")
        f.write("print(q.sqrt(2.5,4))")
        f.close()
        command = "cd "+repo_path+" && python " + basedir + \
            "/inputs/test3.py" + " > "+basedir+"/outputs/test3.txt"
        proc = subprocess.Popen(command, shell=True)
        proc.wait()
        f = open(basedir+"/outputs/test3.txt", 'r+').read().splitlines()
        passed = "False"
        temp = 0
        for x in f:
            if x.find("1.741")!= -1:
                temp += 1
        if temp == 1:
            passed = "True"
            grade+=1
        print(passed)
        f = open(basedir+"/outputs/Total.txt", 'a')
        f.write("\nTest3:"+passed)
        f.close()
    except Exception as e:
        print(e)
#test 4
    try:
        print("\nTest 4 (print(q.exponent(2.5))=12.1824)")
        f = open(basedir+"/inputs/test4.py", 'w+')
        f.write("import sys")
        f.write("\n")
        f.write("sys.path.insert(1,'"+basedir+"')")
        f.write("\n")
        f.write("import equations as q")
        f.write("\n")
        f.write("print(q.exponent(2.5))")
        f.close()
        command = "cd "+repo_path+" && python " + basedir + \
            "/inputs/test4.py" + " > "+basedir+"/outputs/test4.txt"
        proc = subprocess.Popen(command, shell=True)
        proc.wait()
        f = open(basedir+"/outputs/test4.txt", 'r+').read().splitlines()
        passed = "False"
        temp = 0
        for x in f:
            if x.find("12.1824")!= -1:
                temp += 1
        if temp == 1:
            passed = "True"
            grade+=1
        print(passed)
        f = open(basedir+"/outputs/Total.txt", 'a')
        f.write("\nTest4:"+passed)
        f.close()
    except Exception as e:
        print(e)
# test 5
    try:
        print("\nTest 5 (print(q.Ln(1.5))==0.4054)")
        f = open(basedir+"/inputs/test5.py", 'w+')
        f.write("import sys")
        f.write("\n")
        f.write("sys.path.insert(1,'"+basedir+"')")
        f.write("\n")
        f.write("import equations as q")
        f.write("\n")
        f.write("print(q.Ln(1.5))")
        f.close()
        command = "cd "+repo_path+" && python " + basedir + \
            "/inputs/test5.py" + " > "+basedir+"/outputs/test5.txt"
        proc = subprocess.Popen(command, shell=True)
        proc.wait()
        f = open(basedir+"/outputs/test5.txt", 'r+').read().splitlines()
        passed = "False"
        temp = 0
        for x in f:
            if x.find("0.4054")!= -1:
                temp += 1
        if temp == 1:
            passed = "True"
            grade+=1
        print(passed)
        f = open(basedir+"/outputs/Total.txt", 'a')
        f.write("\nTest5:"+passed)
        f.close()
    except Exception as e:
        print(e)
# test6
    try:
        print("\nTest 6 (print(q.calculate(1)))==19.0279)")
        f = open(basedir+"/inputs/test6.py", 'w+')
        f.write("import sys")
        f.write("\n")
        f.write("sys.path.insert(1,'"+basedir+"')")
        f.write("\n")
        f.write("import equations as q")
        f.write("\n")
        f.write("print(q.calculate(1))")
        f.close()
        command = "cd "+repo_path+" && python " + basedir + \
            "/inputs/test6.py" + " > "+basedir+"/outputs/test6.txt"
        proc = subprocess.Popen(command, shell=True)
        proc.wait()
        f = open(basedir+"/outputs/test6.txt", 'r+').read().splitlines()
        passed = "False"
        temp = 0
        for x in f:
            if x.find("19.0279")!= -1:
                temp += 1
        if temp==1:
            passed = "True"
            grade+=1
        print(passed)
        f = open(basedir+"/outputs/Total.txt", 'a')
        f.write("\nTest6:"+passed)
        f.close()

    except Exception as e:
        print(e)



# test7
    try:
        print("\nTest 7 (print(q.calculate(0)))==0.0 no sett)")
        f = open(basedir+"/inputs/test7.py", 'w+')
        f.write("import sys")
        f.write("\n")
        f.write("sys.path.insert(1,'"+basedir+"')")
        f.write("\n")
        f.write("import equations as q")
        f.write("\n")
        f.write("print(q.calculate(0))")
        f.close()
        command = "cd "+repo_path+" && python " + basedir + \
            "/inputs/test7.py" + " > "+basedir+"/outputs/test7.txt"
        proc = subprocess.Popen(command, shell=True)
        proc.wait()
        f = open(basedir+"/outputs/test7.txt", 'r+').read().splitlines()
        passed = "False"
        temp = 0
        for x in f:
            if float(x)== 0.0:
                temp += 1
        if temp==1:
            passed = "True"
            grade+=1
        print(passed)
        f = open(basedir+"/outputs/Total.txt", 'a')
        f.write("\nTest7:"+passed)
        f.close()

    except Exception as e:
        print(e)
        

# test8
    try:
        print("\nTest 8 (print(q.calculate(-1)))==0.0 no sett)")
        f = open(basedir+"/inputs/test8.py", 'w+')
        f.write("import sys")
        f.write("\n")
        f.write("sys.path.insert(1,'"+basedir+"')")
        f.write("\n")
        f.write("import equations as q")
        f.write("\n")
        f.write("print(q.calculate(-1))")
        f.close()
        command = "cd "+repo_path+" && python " + basedir + \
            "/inputs/test8.py" + " > "+basedir+"/outputs/test8.txt"
        proc = subprocess.Popen(command, shell=True)
        proc.wait()
        f = open(basedir+"/outputs/test8.txt", 'r+').read().splitlines()
        passed = "False"
        temp = 0
        for x in f:
            if float(x)== 0.0:
                temp += 1
        if temp==1:
            passed = "True"
            grade+=1
        print(passed)
        f = open(basedir+"/outputs/Total.txt", 'a')
        f.write("\nTest7:"+passed)
        f.close()

    except Exception as e:
        print(e)
    print("Total Grade", (grade/total)*100, "%")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main()
    else:
        print("you need write python check_submition.py hw-id.py while id is your id number")
