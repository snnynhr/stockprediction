## Prepare data

    py prepare-data.py tickerStock.json > training-466.json

## Training MRF

    py mrf.py learning training-85.json 85.model --l2 0.1
    py mrf.py learning training-466.json 466-l2_1.model --l2 1


## Inference

### 466 model

    py mrf.py inference 466-l2_1.model ~/xiaote/stockprediction/newData/weightAll ~/xiaote/stockprediction/newData/test --prune-entropy 1 --annealing 1

### 85 model

THIS STUFF IS OUTDATED. IGNORE.

    py mrf.py inference 85.model ~/xiaote/stockprediction/new_result/reg_result ~/xiaote/stockprediction/new_result/testData --prune-entropy 1 --annealing 1  # 0.5
    py mrf.py inference 85.model ~/xiaote/stockprediction/new_result/reg_result ~/xiaote/stockprediction/new_result/testData --prune-entropy 0.75 --annealing 1  # 0.5
    py mrf.py inference 85.model ~/xiaote/stockprediction/new_result/reg_result ~/xiaote/stockprediction/new_result/testData --prune-entropy 0.5 --annealing 1  # .53
    py mrf.py inference 85.model ~/xiaote/stockprediction/new_result/reg_result ~/xiaote/stockprediction/new_result/testData --prune-entropy 0.25 --annealing 1  # .5
    py mrf.py inference 85.model ~/xiaote/stockprediction/new_result/reg_result ~/xiaote/stockprediction/new_result/testData --prune-entropy 0 --annealing 1  # .52

    py mrf.py inference 85.model ~/xiaote/stockprediction/new_result/reg_result ~/xiaote/stockprediction/new_result/testData --prune-entropy 0.5 --annealing 1.25  # 0.5
    py mrf.py inference 85.model ~/xiaote/stockprediction/new_result/reg_result ~/xiaote/stockprediction/new_result/testData --prune-entropy 0.5 --annealing 1.5  # 0.51
    py mrf.py inference 85.model ~/xiaote/stockprediction/new_result/reg_result ~/xiaote/stockprediction/new_result/testData --prune-entropy 0.5 --annealing 2  # 0.5

    py mrf.py inference 85.model ~/xiaote/stockprediction/new_result/reg_result ~/xiaote/stockprediction/new_result/testData --prune-entropy 0.25 --annealing 2  # 0.53
    py mrf.py inference 85.model ~/xiaote/stockprediction/new_result/reg_result ~/xiaote/stockprediction/new_result/testData --prune-entropy 0.25 --annealing 2.5  # 0.52
    py mrf.py inference 85.model ~/xiaote/stockprediction/new_result/reg_result ~/xiaote/stockprediction/new_result/testData --prune-entropy 0.25 --annealing 3  # 0.52

    # Average: 0.49, Down: 0.55, Up: 0.44
    py mrf.py inference 85.model ~/xiaote/stockprediction/new_result/reg_result ~/xiaote/stockprediction/new_result/testData --prune-entropy 0.5 --annealing 3

    # Average: 0.49, Down: 0.54, Up: 0.44
    py mrf.py inference 85.model ~/xiaote/stockprediction/new_result/reg_result ~/xiaote/stockprediction/new_result/testData --prune-entropy 0.5 --annealing 1

    # Average: 0.51, Down: 0.78, Up: 0.24
    py mrf.py inference 85.model ~/xiaote/stockprediction/new_result/reg_result ~/xiaote/stockprediction/new_result/testData --prune-entropy 0.75 --annealing 1

    # Average: 0.54, Down: 0.09, Up: 0.89
    py mrf.py inference 85.model ~/xiaote/stockprediction/new_result/reg_result ~/xiaote/stockprediction/new_result/testData --prune-entropy 0.25 --annealing 1

    # fav?
    py mrf.py inference 85.model ~/xiaote/stockprediction/new_result/reg_result ~/xiaote/stockprediction/new_result/testData --prune-entropy 0.25 --annealing 2
