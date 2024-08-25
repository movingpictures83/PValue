import PyPluMA

class PValuePlugin:
   def input(self, filename):
        paramfile = open(filename, 'r')
        params = dict()
        for line in paramfile:
            line = line.strip()
            contents = line.split('\t')
            params[contents[0]] = contents[1]

        self.testfile = PyPluMA.prefix()+"/"+params["testfile"]

        self.permutedir = PyPluMA.prefix()+"/"+params["permutedir"]
        self.numperms = int(params["numperms"])
        self.permutefile = params["permutefile"]

   def run(self):
       sum = 1 # count itself
       tf = open(self.testfile, 'r')
       tf.readline()
       y = tf.readline().strip().split(',')
       self.val = float(y[1])
       for i in range(self.numperms):
           #testfile = open(self.permutedir+"/"+str(i)+"/"+self.testfile, 'r')
           # For now assume the value is the first one in the CSV
           #testfile.readline()
           #y = testfile.readline().strip().split(',')
           #self.val = float(y[1])
           permfile = open(self.permutedir+"/"+str(i)+"/"+self.permutefile, 'r')
           permfile.readline()
           x = permfile.readline().strip().split(',')
           value = float(x[1])
           if (value <= self.val):
               sum += 1
               #print("LESS: "+str(value)+" "+str(self.val))
           #else:
               #print("GREATER: "+str(value)+" "+str(self.val))
       self.pvalue = (float(sum)) / float(self.numperms+1)
       print(PyPluMA.prefix()+" NUMBER LESS: "+str(sum)+" VALUE: "+str(self.val))
       print(self.pvalue)

   def output(self, filename):
       outfile = open(filename, 'w')
       outfile.write("\"\",\"Value\"\n")
       outfile.write("\"PValue\","+str(self.pvalue))
