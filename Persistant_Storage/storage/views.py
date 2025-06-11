import json
import re
from json.decoder import JSONDecodeError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.


def home(request):
    return JsonResponse({'message': 'Home page reached'})

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            age = data.get('age')

            if not name or not email or not age:
                return JsonResponse({'error': 'missing field'}, status=400)

            EMAIL_REGEX = r"^[^@]+@[^@]+\.[^@]+$"

            if not re.match(EMAIL_REGEX, email):
                return JsonResponse({'error': 'Invalid email address'})

            user = User.objects.create(name=name, email=email, age=age)
            return JsonResponse({
                'message': 'user created successfully',
                'userId': user.id,
                'name': user.name,
                'email': user.email,
                'age': user.age
            }, status=201)
        except json.JSONDecodeError as e:
            return JsonResponse({
                'error msg': e.msg
            }, status=400)
        except Exception as e:
            return JsonResponse({
                'error': str(e)
            }, status=500)
    return JsonResponse({'error': f'{request.method} method not allowed'}, status=405)

@csrf_exempt
def user_data(request, uid):
    try:
        user = User.objects.get(id=uid)
    except ObjectDoesNotExist:
        return JsonResponse(
                {'error': 'User not found'},
                status=404
                )
    
    if request.method == 'GET':
        return JsonResponse(
            {
            'name': user.name, 
            'email': user.email, 
            'age': user.age
            }, status=200
        )
            
    elif request.method == 'PUT':
        try:
            new_data = json.loads(request.body)
  
            user.name = new_data.get('name', user.name)
            user.email = new_data.get('email', user.email)
            user.age = new_data.get('age', user.age)
            user.save()

            print(user.__dict__)
            return JsonResponse({'message': 'User successfully updated',
            'name': user.name,
            'email': user.email,
            'age': user.age
            }, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'invalid json data passed'}, status=400)
    

    elif request.method == 'DELETE':
        user.delete()
        return JsonResponse({'message': 'User successfully deleted'}, status=200)

    return JsonResponse({'error': 'method not allowed'}, status=405)

@csrf_exempt
def all_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        print(users)

        user_list = [
            {
                'id': str(user.id),
                'name': user.name,
                'email': user.email,
                'age': user.age
            }
            for user in users
        ]
        return JsonResponse({
            'users': user_list
        }, status=200)
    return JsonResponse({'error': f'{request.method} method is not allowed'}, status=405)