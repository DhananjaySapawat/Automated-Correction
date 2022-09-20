import pickle
pred_acc = open('data/pred.txt',"r")
inp_acc = open('data/input.txt',"r")
out_acc= open('data/output.txt',"r")
pred_cost = open('data/pred.txt',"r")
inp_cost = open('data/input.txt',"r")
out_cost= open('data/output.txt',"r")
pred_cost_full = open('data/pred.txt',"r")
inp_cost_full = open('data/input.txt',"r")
out_cost_full= open('data/output.txt',"r")

lm_file = "./data/lm_model.pkl"
with open(lm_file, 'rb') as fp:
   lm_model = pickle.load(fp)

lm_model.unk_prob = 1e-20
lm_model.set_mode('spell_check')

data1= pred_acc.read()
list1= data1.split()
lines1= pred_acc.readlines()
data2= out_acc.read()
list2= data2.split()
lines2= out_acc.readlines()
data3= inp_acc.read()
list3= data3.split()
lines3= inp_acc.readlines()
total = len(list1)
acc = total
acc1 = total
words=0
incwords=0
counter=0
input_file= inp_cost_full.read()
prediction_file = pred_cost_full.read()
target_file= out_cost_full.read()
print(f"Files: Input Score: {lm_model(input_file):.2f} | Prediction Score: {lm_model(prediction_file):.2f} | Target Score: {lm_model(target_file):.2f}" )

while True:
   input_sentence = inp_cost.readline()
   prediction_sentence = pred_cost.readline()
   target_sentence = out_cost.readline()
   counter+=1
   if not input_sentence:
      break
   print(f"Sentence #{counter}: Input Score: {lm_model(input_sentence):.2f} | Prediction Score: {lm_model(prediction_sentence):.2f} | Target Score: {lm_model(target_sentence):.2f}" )

for i in range(len(list1)):

   if(list3[i]!=list2[i]):
      incwords+=1
   if(list1[i]!=list2[i]):
      acc-=1
   if(list3[i]!=list2[i]):
      acc1-=1
   if(list1[i]!=list3[i] and list1[i]==list2[i]):
      words+=1
print("initial incorrect words=",incwords)
print("words corrected=", words)
print("initial accuracy=",acc1/total*100)
print("accuracy final =",(acc/total)*100)
pred_acc.close()
out_acc.close()
inp_acc.close()
