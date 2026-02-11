from loader import load_all_images
from features import extract_features
from similarity import cosine_similarity
ai_images, artist_images = load_all_images()

# Take one image from each
ai_feat = extract_features(ai_images[0])
artist_feat = extract_features(artist_images[0])

print("AI feature shape:", ai_feat.shape)
print("Artist feature shape:", artist_feat.shape)
similarity_score = cosine_similarity(ai_feat, artist_feat)
print("Style similarity score:", similarity_score)