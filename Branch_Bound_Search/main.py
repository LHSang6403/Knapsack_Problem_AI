import os
import sys
import BranchBoundSearching
import HandleBNB

def main():
    current_dir = os.getcwd()
    sys.path.append(current_dir)
    inputFile = os.path.join(current_dir, 'INPUT_7.txt')
    outputFile = os.path.join(current_dir, "Branch_Bound_Search", 
                              "OUTPUT_7.txt")

    BNB = BranchBoundSearching.Problem()
    HandleBNB.SolveKnapsackUsingBNB(BNB, inputFile, outputFile)

main() 