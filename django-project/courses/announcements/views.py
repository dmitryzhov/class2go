from django.http import HttpResponse, Http404from django.shortcuts import render_to_responsefrom django.template import Context, loaderfrom django.template import RequestContextfrom c2g.models import *from courses.common_page_data import get_common_page_datadef list(request, course_prefix, course_suffix):    try:        common_page_data = get_common_page_data(request, course_prefix, course_suffix)    except:        raise Http404            announcements = Announcement.objects.getByCourse(common_page_data['course'])        return render_to_response('announcements/list.html', {'common_page_data':common_page_data, 'announcements':announcements}, context_instance=RequestContext(request))    def admin(request, course_prefix, course_suffix):    try:        common_page_data = get_common_page_data(request, course_prefix, course_suffix)    except:        raise Http404            if not common_page_data['is_course_admin']:        return redirect('courses.views.main', course_prefix, course_suffix)        announcements = Announcement.objects.getByCourse(common_page_data['course'])        return render_to_response('announcements/admin.html', {'common_page_data':common_page_data, 'announcements':announcements}, context_instance=RequestContext(request))    def edit(request, course_prefix, course_suffix, announcement_id):    try:        common_page_data = get_common_page_data(request, course_prefix, course_suffix)    except:        raise Http404            announcement = Announcement.objects.get(id=announcement_id)        return render_to_response('announcements/edit.html', {'common_page_data':common_page_data, 'announcement':announcement}, context_instance=RequestContext(request)) 