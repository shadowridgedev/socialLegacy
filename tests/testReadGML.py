import social as S, os
ENV=os.environ["PATH"]
import  importlib
from IPython.lib.deepreload import reload as dreload
importlib.reload(S.utils)
#dreload(S)
os.environ["PATH"]=ENV

fg=S.GDFgraph() # graph should be on fg.G
