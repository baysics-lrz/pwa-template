from django.shortcuts import render
from django.views.generic import TemplateView
# imported the models for the observations
from observations.models import Category1, Category2, Category3, Category4
from accounts.models import User
from messenger.models import ReportMessage
# Create your views here.
from datetime import datetime

class MapPageView(TemplateView):

    def buildcontext(self, request):
        # Build context items and return with a request to the template
         # All entries from the model
        category1_list = Category1.objects.all()
        category2_list = Category2.objects.all()
        category3_list = Category3.objects.all()
        category4_list = Category4.objects.all()
        # this is compared with the user id in the model
        active_user = request.user.id
        user_list = User.objects.all()
        # user_displayed = {}
        users_with_agreement_list =[]

        # make a new dict to always sort the query by user id
        for u in user_list:
            print(u, u.id, u.name_agreement, u.username)
            # check if they have the name agreement checked or if it is a deleted
            if  u.name_agreement == "Yes" and  "deleted_user_" not in u.username:
                users_with_agreement_list.append(u)

        context = {
            "category1_list": category1_list,
            "category2_list": category2_list,
            "category3_list": category3_list,
            "category4_list": category4_list,
            "active_user": active_user,
            "userswal": users_with_agreement_list,
        }
        return context


    # The "get" method of the views
    def get(self, request):
        context = self.buildcontext(request)
        return render(request, "map.html", context)

    # Post method for the map (so far used for report/flag)
    def post(self, request):
        obs_model = None
        obs_n = 0 #id of the observation
        flag_val = 0
        report_title = ""

        print("============================================flag===============================================")

        # Retrieve information from the post method from map.html and select
        requestlist = request.POST.get("flag_entry").split(",")
        print(requestlist)
        obs_type = requestlist[0]
        obs_n = int(requestlist[1])
        flag_val = int(requestlist[2])
        flag_comment = str(requestlist[3])
        # add user to report
        flag_user = User.objects.get(id = int(requestlist[4]))
        report_model = ReportMessage # Model for report table
        # look if there are preexisting reports
        print(obs_n, flag_val,flag_comment)
        if report_model.objects.all().exists():
            print("previous existing reports")
            previous_report = report_model.objects.all()[report_model.objects.all().count()-1]
            # for a new id count up from the last id
            new_reportID = int(previous_report.id) + 1
        else:
            new_reportID = 1
            print("first reports")
        if flag_val == 1:
            report_title = "Wrong image "
        elif flag_val == 2:
            report_title = "Wrong value "
        elif flag_val == 3:
            report_title = "Others "
        elif flag_val == 4:
            report_title = "high measuring inaccuracy "

        if obs_type == "category1":
            obs_model = Category1
            report_title = report_title + "category1"
        if obs_type == "category2":
            obs_model = Category2
            report_title = report_title + "category2"
        if obs_type == "category3":
            obs_model = Category3
            report_title = report_title + "category3"
        if obs_type == "category4":
            obs_model = Category4
            report_title = report_title + "category4"
        print(report_title)
        # Select observation entry by id
        print(obs_type)
        print(obs_model)
        print("selected entry")
        for it in obs_model.objects.all():
            print(it)
        #print(type(obs_n))
        print(obs_n)
        #print(obs_model.objects.get(id = obs_n))
        entry = obs_model.objects.get(id = obs_n)
        print(entry)
        entry.Flag = flag_val
        # Build the report
        rdate = datetime.today().strftime("%Y-%m-%d")
        # in some cases the auto creation of date in models doesn't work so I added it again
        new_report = report_model(id = new_reportID, date_created = rdate, title = report_title, text = flag_comment, author = flag_user) # insert date
        print(new_report)
        # Safety in case somebody sets the logged_in varibale in the console in
        # the browser to true
        if request.user.id >= 1:
            print("trying to save new report")
            new_report.save()
            #enter the reportid in the observation
            entry.PublicComment = report_model.objects.get(id = new_reportID)
            entry.save()
            print("change in entry")
            print(entry)
            print("finished saving report")
        context = self.buildcontext(request)
        return render(request, "map.html", context)
