#Людмила Жмурова, 37 когорта - Финальный проект. Инженер по тестированиваю плюс

import sender_stand_request
import data

def test_get_by_track():
    create_response = sender_stand_request.create_order(data.order_data)
    assert create_response.status_code == 201  
    track = create_response.json()["track"]     
    get_response = sender_stand_request.get_order_by_track(track)
    assert get_response.status_code == 200  
