from django.test import TestCase, Client
from model_mommy import mommy
from django.utils.timezone import datetime
from .models import Scheduling, Patient, Procedure
from .serializers import PatientSerializer, ProcedureSerializer, SchedulingSerializer
from rest_framework.views import status
from rest_framework.reverse import reverse
import json


# Model tests

class SchedulingModelTest(TestCase):
    """
    Class to test the model
    Scheduling
    """

    def setUp(self):
        """Define the test client and other test variables."""
        self.scheduling = mommy.make(Scheduling)

    def test_scheduling_creation(self):
        """Test the scheduling model can create a scheduling."""
        self.assertTrue(isinstance(self.scheduling, Scheduling))
        self.assertEquals(self.scheduling.__str__(), self.scheduling.date)


class PatientModelTest(TestCase):
    """
    Class to test the model
    Patient
    """

    def setUp(self):
        """Define the test client and other test variables."""
        self.patient = mommy.make(Patient)

    def test_patient_creation(self):
        """Test the patient model can create a patient."""
        self.assertTrue(isinstance(self.patient, Patient))
        self.assertEqual(self.patient.__unicode__(), self.patient.name)
        self.assertEquals(self.patient.__str__(), self.patient.name)


class ProcedureModelTest(TestCase):
    """
    Class to test the model
    Procedure
    """

    def setUp(self):
        """Define the test client and other test variables."""
        self.procedure = mommy.make(Procedure)

    def test_patient_creation(self):
        """Test the procedure model can create a procedure."""
        self.assertTrue(isinstance(self.procedure, Procedure))
        self.assertEqual(self.procedure.__unicode__(), self.procedure.name)
        self.assertEquals(self.procedure.__str__(), self.procedure.name)


# Views tests

class BaseViewTest(TestCase):

    def setUp(self):
        """Define the test client and other test variables."""
        patient = Patient.objects.create(name='application patient')
        procedure = Procedure.objects.create(name='can be deployed')
        self.valid_data = {
            'date': '2018-08-02',
            'initial_time': '02:02:00',
            'final_time': '03:03:00',
            'patient': patient.id,
            'procedure': procedure.id
        }
        self.invalid_data = {
            'date': '',
            'initial_time': '',
            'final_time': '',
            'patient': '',
            'procedure': ''
        }
        self.response = self.client.post(
            reverse(
                "scheduling-list",
            ),
            data=json.dumps(self.valid_data),
            content_type="application/json"
        )

    def test_scheduling_post(self):
        """Test the post method for scheduling data."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        # test with invalid data
        response = self.client.post(
            reverse(
                "scheduling-list",
            ),
            data=json.dumps(self.invalid_data),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_scheduling_get(self):
        """Test the get method in a given scheduling."""
        scheduling = Scheduling.objects.first()
        response = self.client.get(
            scheduling.get_api_url(),
            data={},
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_scheduling_get_all(self):
        response = self.client.get(
            reverse(
                "scheduling-list"
            )
        )
        expected = Scheduling.objects.all()
        serialized = SchedulingSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_scheduling_update(self):
        """Test the update method in a given scheduling."""
        scheduling = Scheduling.objects.first()
        response = self.client.put(
            scheduling.get_api_url(),
            data=json.dumps(self.valid_data),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_scheduling_delete(self):
        """Test the delete method in a given scheduling."""
        scheduling = Scheduling.objects.first()
        response = self.client.delete(
            scheduling.get_api_url(),
            content_type="application/json",
            follow=True
        )
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
