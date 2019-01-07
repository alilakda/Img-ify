def detect_labels_uri(uri):
    """Detects labels in the file located in Google Cloud Storage or on the
    Web."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = uri

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')

    # for label in labels:
    #     print(label.description)
    label_list = []
    for label in labels:
        if len(label_list) <= 2:
            label_list.append(label.description)

    return(label_list)
    print(label_list)


detect_labels_uri('https://i.ytimg.com/vi/SfLV8hD7zX4/maxresdefault.jpg')


