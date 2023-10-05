from pydantic import BaseModel


class URLItem(BaseModel):
    link: str

response_data = [URLItem(link='andrea')]
link_value = response_data[0].link
print(link_value)



