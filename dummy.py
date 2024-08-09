.menu-link {
    text-decoration: none;
    color: white;
    position: absolute;
    left: 20px;
    top: 50%;
    transform: translateY(-50%);
    display: flex;
    align-items: center;
    font-size: 16px;
}

.menu-link i {
    margin-right: 5px;
}
    file_list = [item['Key'] for item in response['Contents'] if item['Key'] != folder_name]
