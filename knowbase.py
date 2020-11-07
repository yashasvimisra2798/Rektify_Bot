# imports 
import os
import time
import dotenv
from azure.cognitiveservices.knowledge.qnamaker.authoring import QnAMakerClient
from azure.cognitiveservices.knowledge.qnamaker.runtime import QnAMakerRuntimeClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.knowledge.qnamaker.authoring.models import QnADTO, UpdateKbOperationDTOAdd, UpdateQnaDTO
from azure.cognitiveservices.knowledge.qnamaker.authoring.models import OperationStateType, UpdateKbOperationDTO
from azure.cognitiveservices.knowledge.qnamaker.authoring.models import UpdateKbOperationDTOUpdate, UpdateQnaDTOQuestions

# .env init
dotenv.load_dotenv()

# load QNAMaker Variables
subscription_key = os.getenv('QNA_SUB_KEY')
host = os.getenv('QNA_HOST')
kb_id = os.getenv('QNA_KB_ID')
kb_name = os.getenv('QNA_KB_NAME')

# function to monitor initiated operation
def _monitor_operation(client, operation):
    for i in range(20):
        if operation.operation_state in [OperationStateType.not_started, OperationStateType.running]:
            print("Waiting for operation: {} to complete.".format(operation.operation_id))
            time.sleep(5)
            operation = client.operations.get_details(operation_id=operation.operation_id)
        else:
            break
    if operation.operation_state != OperationStateType.succeeded:
        raise Exception("Operation {} failed to complete.".format(operation.operation_id))
    return operation

# function to publish kb
def publish_kb(client, kb_id):
    client.knowledgebase.publish(kb_id=kb_id)

# function to add a new question to existing answer and publish kb
def updateQNA(_id, newQ):
    try:
        client = QnAMakerClient(endpoint = host, credentials = CognitiveServicesCredentials(subscription_key))
        print("Updating KB...")
        update_kb_operation_dto = UpdateKbOperationDTO(
            update = UpdateKbOperationDTOUpdate(
                name = kb_name,
                qna_list=[
                    UpdateQnaDTO(
                        id=_id,
                        questions=UpdateQnaDTOQuestions(
                            add=[newQ]
                        )   
                    )
                ]
            )
        )
        update_op = client.knowledgebase.update(kb_id = kb_id, update_kb = update_kb_operation_dto)
        _monitor_operation(client = client, operation = update_op)
        print("KB Updated.")
        print("Publishing KB...")
        publish_kb(client, kb_id)
        print("KB Published")
        print()
        return True
    except:
        return False
    
# function to add a new question and answer pair and publish kb
def addNewQNA(que, ans):
    try:
        client = QnAMakerClient(endpoint = host, credentials = CognitiveServicesCredentials(subscription_key))
        print("Updating KB...")
        update_kb_operation_dto = UpdateKbOperationDTO(
            add = UpdateKbOperationDTOAdd(
                qna_list=[
                    QnADTO(questions = [que], answer = ans)
                ]
            )
        )
        update_op = client.knowledgebase.update(kb_id = kb_id, update_kb = update_kb_operation_dto)
        _monitor_operation(client = client, operation = update_op)
        print("Publishing KB...")
        publish_kb(client, kb_id)
        print("KB Published")
        return True
    except:
        return False