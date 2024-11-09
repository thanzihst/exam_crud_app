from django.shortcuts import render,redirect
from django.views import View
from store.forms import RealEstateCreateForm
from store.models import RealEstate

# Create your views here.


class RealEstateCreate(View):

    template_name="realestatecreate.html"

    form_class=RealEstateCreateForm

    def get(self,request,*args,**kwargs):

        form_instance=self.form_class

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=self.form_class(form_data,files=request.FILES)

        if form_instance.is_valid():

            form_instance.save()

            

            return redirect("property-list")
        
        return render(request,self.template_name,{"form":form_instance})
    

        

class RealEstateList(View):

    template_name="realestatelist.html"

    def get(self,request,*args,**kwargs):

        qs=RealEstate.objects.all()

        return render(request,self.template_name,{"data":qs})
    


class RealEstateUpdate(View):

    template_name="realestateupdate.html"

    form_class=RealEstateCreateForm

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        estate_object=RealEstate.objects.get(id=id)

        form_instance=self.form_class(instance=estate_object)
        return render(request,self.template_name,{"form":form_instance})

    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")

        estate_object=RealEstate.objects.get(id=id)

        form_data=request.POST

        form_instance=self.form_class(form_data,files=request.FILES,instance=estate_object)

        if form_instance.is_valid():
           
            form_instance.save()

            return redirect("property-list")
        
        return render(request,self.template_name,{"form":form_instance})
    

class RealEstateDelete(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        RealEstate.objects.get(id=id).delete()

        return redirect("property-list")





        