from concurrent.futures import ThreadPoolExecutor
import os
import pandas as pd
from .config import RAW_AUDIO_DIR, ROOT_DIR, DATA_DIR

def extract_filename_info(actor_folder):
    """Retrieves the descriptive information from the name of the given file. 
    
    Returns:
    -------- 
    data : list
        A list of dictionaries containing column labels and values for the given file.
    """
    data = []
    full_path = os.path.join(RAW_AUDIO_DIR, actor_folder)
    for file in os.listdir(full_path):
        parts = file.replace(".wav", "").split("-")

        data.append({
                    "file_name": file,
                    "modality": parts[0],
                    "vocal_channel": parts[1],
                    "emotion": parts[2],
                    "intensity": parts[3],
                    "statement": parts[4],
                    "repetition": parts[5],
                    "actor": parts[6]
                })
    return data 

def main():

    # obtain all information from file names  
    actor_list = [f for f in os.listdir(RAW_AUDIO_DIR) if os.path.isdir(os.path.join(RAW_AUDIO_DIR, f))]
    all_data = []
    with ThreadPoolExecutor() as executor: 
        results = executor.map(extract_filename_info, actor_list)
        for res in results:
            all_data.extend(res)

    # create dataframe
    df_audio = pd.DataFrame(all_data)

    # decode required columns 
    emotion_map = {
        '01': 'neutral',
        '02': 'calm',
        '03': 'happy',
        '04': 'sad',
        '05': 'angry',
        '06': 'fearful',
        '07': 'disgust',
        '08':'surprised'
    }
    intensity_map = {
        '01': 'normal',
        '02': 'strong',
    }
    actor_map = {f"{i:02}": i for i in range(1, 25)}

    df_audio['emotion'] = df_audio['emotion'].map(emotion_map)
    df_audio['intensity'] = df_audio['intensity'].map(intensity_map)
    df_audio['actor'] = df_audio['actor'].map(actor_map)

    # save dataframe as csv 
    df_audio.to_csv(os.path.join(DATA_DIR, 'processed_data.csv'), index=False)

if __name__ == "__main__":
    main() 