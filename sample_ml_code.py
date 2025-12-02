"""
Sample ML script with security-related patterns for testing forensics logging.
"""
import pickle
import torch
import numpy as np

def load_model():
    # This will trigger MODEL_LOAD detection
    model = torch.load('model.pth')
    return model

def load_data():
    # This will trigger DATA_LOAD detection
    with open('data.pkl', 'rb') as f:
        data = pickle.load(f)
    
    # This will also trigger DATA_LOAD detection
    array = np.load('data.npy')
    
    return data, array

if __name__ == '__main__':
    model = load_model()
    data, array = load_data()
