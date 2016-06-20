import fnmatch
import os
import subprocess

'''
The program takes three required arguments:
    1.  The directory of your PTB/Tree files (will recursively walk this folder for all files and subdirectories)
    2.  The file ending of your PTB/tree files in the directory
    3. The path to your Stanford CoreNLP folder (with a trailing slash)
'''
matches = []
for root, dirnames, filenames in os.walk(sys.argv[1]):
    for filename in fnmatch.filter(filenames, sys.argv[2]):
        matches.append(os.path.join(root, filename))

number_of_files = len(matches)
for idx, tree in enumerate(matches):
    print "File " + idx + " out of  " + number_of_files +" files"
    command = 'java -mx150m -cp ' + sys.argv[3] + '* edu.stanford.nlp.trees.EnglishGrammaticalStructure -treeFile ' + tree + ' -conllx'
    try:
            result = subprocess.check_output(command.split(" ") , stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
    #save result file as file
    #base=os.path.basename(tree)
    #filename = os.path.splitext(base)

    with open(os.path.splitext(tree)[0] +  '.conll', 'w') as resultfile:
        resultfile.write(result)
        resultfile.close()
