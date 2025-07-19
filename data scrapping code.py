with open('smartprix.html','r',encoding='utf-8') as f:
  html=f.read()
from bs4 import BeautifulSoup
soup.prettify()
items=soup.find_all('div',{'class':'sm-product has-tag has-features has-actions'})
import numpy as np
import pandas as pd
name=[]
price=[]
specs_score=[]
sim=[]
processor=[]
ram=[]
battery=[]
display=[]
camera=[]
memory_card=[]
android_v=[]
for i in items:
  name.append(i.find('h2').text)
  price.append(i.find('span',{'class':'price'}).text)
  specs_score.append(i.find('div',{'class':'tags'}).find('b').text)
  specs=(i.find('ul',{'class':'sm-feat specs'}).find_all('li'))
  try:
      sim.append(specs[0].text)
  except:
      sim.append(np.nan)

  try:
      processor.append(specs[1].text)
  except:
      processor.append(np.nan)

  try:
      ram.append(specs[2].text)
  except:
      ram.append(np.nan)

  try:
      battery.append(specs[3].text)
  except:
      battery.append(np.nan)

  try:
      display.append(specs[4].text)
  except:
      display.append(np.nan)

  try:
      camera.append(specs[5].text)
  except:
      camera.append(np.nan)

  try:
      memory_card.append(specs[6].text)
  except:
      memory_card.append(np.nan)

  try:
      android_v.append(specs[7].text)
  except:
      android_v.append(np.nan)
    
df=pd.DataFrame({
    'name':name,
    'price':price,
    'specs_score':specs_score,
    'sim':sim,
    'processor':processor,
    'ram':ram,
    'battery':battery,
    'display':display,
    'camera':camera,
    'memory_card':memory_card,
    'android_version':android_v
})
df.to_csv('phones.csv',index=False,encoding='utf-8-sig')
