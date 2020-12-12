import sys
import json
import os

def remove_directory(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))

def json_to_something(j_file, r_dir):
    for i in j_file:
        if str(j_file[i])[0] == "{":
            path = r_dir + "\\" + str(i)
            try:
                os.mkdir(path)
            except OSError:
                print ("Directory %s already exists... deleting it and recreating it..." % path)
            finally:
                remove_directory(path)
                os.rmdir(path)
                os.mkdir(path)
            json_to_something(j_file[i], r_dir + "\\" + str(i))
        else:
            if os.path.exists(r_dir + "\\" + str(i)):
                os.remove(r_dir + "\\" + str(i))
            f = open(r_dir + "\\" + str(i), "a")
            f.write(str(j_file[i]))
            f.close()

def check_argv_number():
    if len(sys.argv) != 3:
        return False
    else:
        return True

def check_second_argv():
    if os.path.isdir(sys.argv[1]):  
        return True
    return False

def check_third_argv():
    if os.path.isfile(sys.argv[2]):  
        return True
    return False

def main():
    if check_argv_number() and check_second_argv() and check_third_argv():
        root_dir = sys.argv[1]
        f = open(sys.argv[2], "r")
        try:
            json_file = json.loads(str(f.read()))
        except:
            print("String could not be converted to JSON")
            return False
        f.close()
        json_to_something(json_file, root_dir)
    else:
        print("You have to pass in 3 arguments:")
        print("- name of this script;")
        print("- the path where you want to create the folder structure;")
        print("- the path of the JSON file.")

main()


# some JSON:
# x = '{"dir1": {"dir2": {"file1": "continut1", "file2": "continut2"}, "file3": "continut3"}, "file4": "continut4"}'
# parse x:
# json_file = json.loads(x)
# root_dir = "C:\\Users\\Subaru\\Desktop\\PythonProject\\root"
# json_to_something(json_file, root_dir)

############################################################################################################################
# python create_structure.py "C:\Users\Subaru\Desktop\PythonProject\root" "C:\Users\Subaru\Desktop\PythonProject\json.json"
############################################################################################################################

# TO DO:
# - json files could have a longer than 1 line json... check in file... or read the whole file in one take
# - the file/directory tree print