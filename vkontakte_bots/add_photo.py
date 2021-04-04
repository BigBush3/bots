upload  = vk_api.VkUpload(vk_session)
photo = upload.photo_wall(['Picture1.png']
)

vk_photo_id = f"photo{photo[0]['owner_id']}_{photo[0]['id']}"

print(photo, vk_photo_id, sep="\n")
vk = vk_session.get_api()
vk.wall.post(message="Test", attachments=[vk_photo_id])