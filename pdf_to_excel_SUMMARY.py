#!/usr/bin/env python
# coding: utf-8

# In[77]:


from tabula import read_pdf #Libreria para leer pdf como dataframe
from tabulate import tabulate# convertir los datos en tabuladosimport pandas as pd # Sive para manipular dataframes de distintas maneras, es como una barra de herramientas para dataframes
import pandas as pd


# In[123]:


#obtiene dataframes de el pdf
#las medidas de el area se sacaron de la pagina de tabula, se extrae el archivo como script 

documento= "C:\\Users\\bcespedes.ap\\Desktop\\Automatizacion\\SUMMARY OF COMPARISON mt MARLIN MYSTERY (COPEC).pdf"

df0 = read_pdf(documento, pages='2-2' ,stream=True, area=[198.518,68.391,261.248,555.696])

df1 = read_pdf(documento, pages='2-2' ,stream=True, area=[267.368,69.921,336.983,551.87])

df2 = read_pdf(documento, pages='2-2' ,stream=True, area=[338.513,69.921,408.128,553.401])

df3 = read_pdf(documento, pages='2-2' ,stream=True, area=[424.957,66.861,487.687,552.636])

df4 = read_pdf(documento, pages='2-2' ,stream=True, area=[505.282,66.861,566.482,551.871])

df6 = read_pdf(documento, header=False, index=False
, pages='2-2' ,stream=True, area=[93.712,352.971,153.382,551.871])
df1
 
    #"Facturas 'Provisorias o finales' BT 'Nombre_buque' CC 'YY_YY' 


# In[124]:


#Selecciona solo la informacion relevante sin el 'MT'
x=list(df6.columns.values)
y=x[1]
res = y.split(' ', 1)[1] 
res # nuevo nombre sin el 'MT'


# In[125]:


#nombre a cada tabla 
F=df6.rename(columns={ 'MT "MARLIN MYSTERY"': res}) 
df0.rename( columns={'Unnamed: 0':'B|L'}, inplace=True )
df1.rename( columns={'Unnamed: 0':'DISCHARGE IN COMAP MEJILLONES PORT (1° STAGE)','Unnamed: 1':'M3 @ 60 oF','Unnamed: 2':'BARRELS @ 60oF','Unnamed: 3':'DISCHARGE IN COMAP MEJILLONES PORT (1° STAGE)','Unnamed: 4':'DISCHARGE IN COMAP MEJILLONES PORT (1° STAGE)'}, inplace=True )
df2.rename( columns={'Unnamed: 0':'DISCHARGE IN COPEC QUINTERO PORT (2° STAGE)'}, inplace=True )
df3.rename( columns={'Unnamed: 0':'COMPARISONS (BOL versus TERMINALS )'}, inplace=True )
#df4.columns = ['COMPARISONS (VESSEL versus TERMINALS )','M3 @ 60 oF']
A=df0.drop([0])
B=df1.drop([1,0])
C=df2.drop([1,0])
D=df3.drop([0])
E=df4.drop([1])
print(F)
print(A)
print(B)
print(C)
print(D)
print(E)


# In[ ]:





# In[126]:


#imprime en pantalla como se guardaran los dataframes en el excel

print(F)
print(A)
print(B)
print(C)
print(D)
print(E)


# In[127]:


#Se guardan los dataframes en distintas hojas en un mismo excel 
dfs = {'Info_product':F, 'B|L':A , 'Port1':B , 'Port2':C, 'Bol vs terminal':D, 'Vessel vs terminal':E}

out_path = "C:\\Users\\bcespedes.ap\\Desktop\\Automatizacion\\marlin_mistery.xlsx" #agregar path donde esta tu archivo 


writer = pd.ExcelWriter(out_path, engine='xlsxwriter')
for sheet_name in dfs.keys():
    dfs[sheet_name].to_excel(writer, sheet_name=sheet_name, index=False)
    
writer.save()


# In[ ]:





# In[ ]:




