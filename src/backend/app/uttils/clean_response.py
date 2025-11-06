def cleaner(cleaned_response: str):
    if cleaned_response.startswith('```'):
        cleaned_response = cleaned_response.split('\n', 1)[1]
        cleaned_response = cleaned_response.rsplit('```', 1)[0]
        cleaned_response = cleaned_response.strip()
        cleaned_response = cleaned_response.replace('"', '')
        
    
    return cleaned_response