from db.movie_dao import get_reviews
import pandas as pd
from datetime import datetime

reviews = get_reviews()

df_save = pd.DataFrame(reviews)
print(df_save)

now = datetime.now().strftime("%Y%m%d%H%M")
df_save.to_excel(f"./review_save_{now}.xlsx", index=False)