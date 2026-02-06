import pandas as pd
from langchain_core.documents import Document

class Dataconvertor:
    def __init__(self, file_path:str):
        self.file_path= file_path

    def convert(self):
        df= pd.read_csv(self.file_path)[['product_title','review']]
        docs =[ Document(page_content= rows['review'],
                meta_data= {"product_name": rows['product_title']})
             for _, rows in df.iterrows()
              ]
        
        return docs

    

