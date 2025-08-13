from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import Contact
import json

def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            subject = data.get('subject', '')
            message = data.get('message')
            
            if name and email and message:
                # Save the contact form data to database
                contact = Contact.objects.create(
                    name=name,
                    email=email,
                    subject=subject,
                    message=message
                )
                
                # Also log for debugging
                print(f"=== NEW CONTACT FORM SUBMISSION SAVED ===")
                print(f"ID: {contact.id}")
                print(f"Name: {name}")
                print(f"Email: {email}")
                print(f"Subject: {subject}")
                print(f"Message: {message}")
                print(f"Timestamp: {contact.created_at}")
                print(f"=========================================")
                
                return JsonResponse({
                    'success': True,
                    'message': 'Thank you! Your message has been received. I\'ll get back to you soon!',
                    'data': {
                        'id': contact.id,
                        'name': name,
                        'email': email,
                        'subject': subject,
                        'message': message,
                        'timestamp': contact.created_at.isoformat()
                    }
                })
            else:
                return JsonResponse({
                    'success': False,
                    'message': 'Please fill in all required fields.'
                }, status=400)
                
        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'message': 'Invalid data format.'
            }, status=400)
        except Exception as e:
            print(f"Contact form error: {e}")
            return JsonResponse({
                'success': False,
                'message': 'An error occurred. Please try again.'
            }, status=500)
    
    return render(request, 'contact.html')

def education(request):
    return render(request, 'education.html')

def experience(request):
    return render(request, 'experience.html')

def projects(request):
    return render(request, 'projects.html')