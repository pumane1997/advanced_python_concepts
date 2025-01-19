import justpy as jp
import documentation 
import api

jp.Route(path='/', wpfunc=documentation.Documentation.serve)
jp.Route(path='/api', wpfunc=api.API.serve)


jp.justpy()