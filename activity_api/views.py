from django.shortcuts import render
from django.http import JsonResponse
from .models import User, ActivityPeriod

def filter_db(request):

    valid_keys = {"firstname", "lastname", "tz"}
    
    for key in request.GET:
        if key not in valid_keys:
            return []

    users = User.objects.all()
    
    if "firstname" in request.GET:
        users = users.filter(first_name__exact=request.GET["firstname"])

    if "lastname" in request.GET:
        users = users.filter(last_name__exact=request.GET["lastname"])

    if "tz" in request.GET:
        users = users.filter(tz__exact=request.GET["tz"])
        
    return users

def get_user_activity(request):
        
    response_obj = {"ok": False, "members": []}

    users = filter_db(request)

    if len(users) > 0:
        response_obj["ok"] = True

    for u in users:
        
        user_info = {}
      
        user_info["id"] = u.id
        user_info["real_name"] = u.first_name + " " + u.last_name
        user_info["tz"] = u.tz
        user_info["activity_periods"] = [{"start_time": ap.start_time.strftime("%b %d %Y %I:%M%p"), 
                                        "end_time": ap.end_time.strftime("%b %d %Y %I:%M%p")} 
                                        for ap in u.activityperiod_set.all()]

        response_obj["members"].append(user_info)
        
     
    return JsonResponse(response_obj, json_dumps_params={"indent": 4})
