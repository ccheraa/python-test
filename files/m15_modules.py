import modules.test_module as test
from modules.test_module import d_dict
import platform
test.d_list(5, 25, 'me', False)
d_dict(a=5, b=25, c='me', d=False)

print(platform.system())
print(dir(test))