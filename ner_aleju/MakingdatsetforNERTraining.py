
# coding: utf-8

# In[ ]:

C:\Users\nitin.jain\Downloads\entity-annotated-corpus


# In[86]:

data=[]
a=''
skipped=1
with open("C:/Users/nitin.jain/Downloads/entity-annotated-corpus/ner_dataset.txt", "r",encoding='latin-1') as handle:
    for article in handle:
        #print(article)
        if skipped==1:
            skipped=skipped+1
        else:
            intr=article.encode().decode("utf-8").strip().split("\t")
            if intr[0][:8]=="Sentence":
                data.append(a.strip())
                a=''
                if intr[3]!='O':
                    a=a+" "+str(intr[1].strip()+"/"+intr[3].strip())
                else:
                    a=a+" "+intr[1].strip()                         
            else:
                if intr[2]!='O':
                    a=a+" "+str(intr[0].strip()+"/"+intr[2].strip())
                else:
                    a=a+" "+intr[0].strip()       


# In[87]:

import pandas as pd
df=pd.DataFrame(data[1:])
pd.set_option('display.max_colwidth', -1)


# In[90]:

len(df)
df.to_csv(r'C:/Users/nitin.jain/Downloads/entity-annotated-corpus/ner_dataset_processed.txt', header=None, index=None, mode='a', sep='\t')
df.to_csv(r'C:/Users/nitin.jain/Downloads/entity-annotated-corpus/ner_dataset_processed.csv', header=None, index=None, mode='a')


# In[94]:

df.loc[34,]

