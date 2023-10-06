import oci

compartment_id = '<YOUR COMPARTMENT_ID>'
signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()

queue_endpoint = '<YOUR QUEUE_ENDPOINT>'
queue_id = '<YOUR QUEUE_OCID>'
queue_client = oci.queue.QueueClient(config={}, signer=signer, service_endpoint=queue_endpoint)

def publish_message(message_content, publish_channel_id):
    queue_client.put_messages(
        queue_id=queue_id,
        put_messages_details=oci.queue.models.PutMessagesDetails(
            messages = [
                oci.queue.models.PutMessagesDetailsEntry(
                    content = message_content,
                    metadata = oci.queue.models.MessageMetadata(channel_id = publish_channel_id)
                )
            ]
        )
    )

def consume_messages():
    messages = queue_client.get_messages(
        queue_id = queue_id,
        timeout_in_seconds=1,
        limit = 1
    )
    return messages

def delete_messages(messages):
    for message in messages :
        queue_client.delete_message(queue_id, message.receipt)


if __name__ == "__main__":

    print("--- NO-Channel Patern Start ---")
    message_content = "This is a message from P1"

    for i in range(5):
        publish_message(message_content + " - " + str(i + 1), "")

    message_content = "This is a message from P2"
    for i in range(2):
        publish_message(message_content + " - " + str(i + 1), "")

    message_content = "This is a message from P3"
    for i in range(1):
        publish_message(message_content + " - " + str(i + 1), "")

    
    for i in range(10): 
        response = consume_messages()

        for message in response.data.messages: 
            print(message.content)

        delete_messages(response.data.messages)

    print("--- NO-Channel Patern End ---")

    print("--- Channel-Enabled Patern Start ---")

    message_content = "This is a message from P1"
    for i in range(5):
        publish_message(message_content + " - " + str(i + 1), "channel-1")

    message_content = "This is a message from P2"
    for i in range(2):
        publish_message(message_content + " - " + str(i + 1), "channel-2")

    message_content = "This is a message from P3"
    for i in range(1):
        publish_message(message_content + " - " + str(i + 1), "channel-3")

    for i in range(10): 
        response = consume_messages()

        for message in response.data.messages: 
            print(message.content)

        delete_messages(response.data.messages)

    print("--- Channel-Enabled Patern End ---")