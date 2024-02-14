import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import OneHotEncoder
from scipy.spatial import distance
import numpy as np
from datetime import datetime

def get_recommendations(restaurants, user_preferences):
   
    current_time = datetime.now().time()
    # open_restaurants = restaurants[(restaurants['start_time'] <= user_preferences['current_time']) & (restaurants['end_time'] > user_preferences['current_time'])]
    open_restaurants = restaurants
    if open_restaurants.empty:
        print("No restaurants are open at this time.")
        return None

    enc = OneHotEncoder()
    restaurant_features = enc.fit_transform(restaurants[['preferred_cuisines', 'budget', 'city', 'state', 'preferred_ambiance', 'dietary_restrictions']]).toarray()

    user_preferences_adjusted = {
        'preferred_cuisines': user_preferences['preferred_cuisines'][0],
        'budget': user_preferences['budget'],
        'city': user_preferences['city'],
        'state': user_preferences['state'],
        'preferred_ambiance': user_preferences['preferred_ambiance'],
        'dietary_restrictions': user_preferences['dietary_restrictions'][0]
    }
    user_df_adjusted = pd.DataFrame([user_preferences_adjusted])
    user_features = enc.transform(user_df_adjusted).toarray()

    similarity_scores = cosine_similarity(user_features, restaurant_features[open_restaurants.index])

    for feature, enc_feature in zip(['preferred_cuisines', 'budget', 'city', 'state', 'preferred_ambiance', 'dietary_restrictions'], enc.get_feature_names_out()):
        weight = user_preferences['feature_importance'][0] 
        feature_index = np.where(enc_feature == feature)[0]
        if feature_index.size > 0:
            similarity_scores[:, feature_index] *= weight

    similarity_scores = similarity_scores / np.max(similarity_scores)

    user_location = np.array(user_preferences['location_preference'])
    restaurant_locations = np.stack(open_restaurants['coordinates'])
    location_distances = distance.cdist([user_location], restaurant_locations, 'euclidean')[0]

    max_distance = np.max(location_distances)
    normalized_distances = location_distances / max_distance

    max_radius = 10
    filtered_restaurants_index = location_distances <= max_radius
    filtered_restaurants = open_restaurants[filtered_restaurants_index]

    filtered_restaurants['similarity_score'] = similarity_scores[0][filtered_restaurants_index]

    recommended_restaurants = filtered_restaurants.sort_values(by='similarity_score', ascending=False)

    N = 3
    # return recommended_restaurants.head(N)
    return restaurants