from fastapi import FastAPI, HTTPException
import pandas as pd

app = FastAPI()

@app.get("/recommendations/{product_id}")
async def read_recommendations(product_id: str, top_n: int = 5):
    
    # --- Read database for product recommendations
    # item_similarity_df = {}
    
    # --- If product not found, raise error
    if product_id not in item_similarity_df.columns:
        raise HTTPException(status_code=404, detail="Product not found")
    
    # --- Get recommendations
    def get_item_based_recommendations(product_id, top_n):
        similar_scores = item_similarity_df[product_id]
        similar_scores = similar_scores.sort_values(ascending=False)
        similar_scores = similar_scores[similar_scores.index != product_id]
        top_product_ids = similar_scores.head(top_n).index
        
        return top_product_ids.tolist()

    recommendations = get_item_based_recommendations(product_id, top_n)
    
    return {"product_id": product_id, "recommendations": recommendations}
