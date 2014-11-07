
#Remember to Change the Folder!!!!!
DATA_DIR='../updatedXYdata'
EXPR_NUM='2'
EXPR_FOLDER="$DATA_DIR/$EXPR_NUM"

#Change features.py, Ylabel.py, XYmain.py as necessary

#Run XYmain.py

python XYmain.py "${EXPR_FOLDER}" > "${EXPR_NUM}_dia.txt"

#Change partitionP.py partitionS.py as necessary

python partitionP.py "${EXPR_FOLDER}" > "${EXPR_NUM}_p.sh"

sh "${EXPR_NUM}_p.sh"

#Or

#To run partition.py sequentially, 
#Change the folder in partition.py and comment out the following line
#partition.py

#Remember to change l1 value if needed
python regMainBP.py "${EXPR_FOLDER}" 1 > "${EXPR_NUM}_reg.sh"

sh "${EXPR_NUM}_reg.sh"

#Remember to change parseWeight.py before running the script below

python parseWeightP.py > "${EXPR_NUM}_pw.sh"

sh "${EXPR_NUM}_pw.sh"

echo "DONE!"


