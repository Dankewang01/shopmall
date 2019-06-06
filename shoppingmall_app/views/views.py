def publish(request):
    ret = {'status': False, 'data': '', 'error': '', 'summary': ''}
    if request.method == 'POST':
        request_form = PublishForm(request.POST)
        if request_form.is_valid():
            request_dict = request_form.clean()
            print(request_dict)
            ret['status'] = True
        else:
            error_msg = request_form.errors.as_json()
            ret['error'] = json.loads(error_msg)
    return HttpResponse(json.dumps(ret))