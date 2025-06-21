import pytest
from longship_api_client.models.chargepoint_dto_connectivity_status import (
    ChargepointDtoConnectivityStatus,
)
from longship_api_client.models.connector_operational_status_dto_operational_status import (
    ConnectorOperationalStatusDtoOperationalStatus,
)

from longship.types import (
    CDRCreatedData,
    ChargePointBootedData,
    ConnectivityStatusChangedData,
    LocationCreatedData,
    LocationUpdatedData,
    MSPInvoiceProposalStatusData,
    OperationalStatusChangedData,
    PingData,
    RegistrationStatusType,
    SessionStartData,
    SessionStopData,
    SessionUpdateData,
    WebhookPayload,
    WebhookPayloadType,
)


class TestWebhookPayloadType:
    def test_enum_values(self):
        """Test that all webhook payload types have correct string values."""
        assert str(WebhookPayloadType.ChargePointBooted) == "ChargePointBooted"
        assert str(WebhookPayloadType.OperationalStatusChanged) == "OperationalStatusChanged"
        assert str(WebhookPayloadType.ConnectivityStatusChanged) == "ConnectivityStatusChanged"
        assert str(WebhookPayloadType.SessionStart) == "SessionStart"
        assert str(WebhookPayloadType.SessionUpdate) == "SessionUpdate"
        assert str(WebhookPayloadType.SessionStop) == "SessionStop"
        assert str(WebhookPayloadType.CDRCreated) == "CdrCreated"
        assert str(WebhookPayloadType.LocationCreated) == "LocationCreated"
        assert str(WebhookPayloadType.LocationUpdated) == "LocationUpdated"
        assert str(WebhookPayloadType.MSPInvoiceProposalStatus) == "MspInvoiceProposalStatus"
        assert str(WebhookPayloadType.Ping) == "Ping"


class TestRegistrationStatusType:
    def test_enum_values(self):
        """Test that registration status types have correct string values."""
        assert str(RegistrationStatusType.Accepted) == "Accepted"
        assert str(RegistrationStatusType.Pending) == "Pending"


class TestDataClasses:
    def test_charge_point_booted_data(self):
        """Test ChargePointBootedData creation and attributes."""
        data = ChargePointBootedData(registrationstatus=RegistrationStatusType.Accepted)
        assert data.registrationstatus == RegistrationStatusType.Accepted

    def test_operational_status_changed_data(self):
        """Test OperationalStatusChangedData creation and attributes."""
        data = OperationalStatusChangedData(
            status=ConnectorOperationalStatusDtoOperationalStatus.AVAILABLE,
            errorcode="NoError",
            connectornumber=1,
            statussource="Local",
            locationid="loc123",
            evseid="evse123",
            vendorid="vendor123",
            vendorerrorcode="vendor_error"
        )
        assert data.status == ConnectorOperationalStatusDtoOperationalStatus.AVAILABLE
        assert data.errorcode == "NoError"
        assert data.connectornumber == 1
        assert data.statussource == "Local"
        assert data.locationid == "loc123"
        assert data.evseid == "evse123"
        assert data.vendorid == "vendor123"
        assert data.vendorerrorcode == "vendor_error"

    def test_operational_status_changed_data_optional_fields(self):
        """Test OperationalStatusChangedData with optional fields as None."""
        data = OperationalStatusChangedData(
            status=ConnectorOperationalStatusDtoOperationalStatus.AVAILABLE,
            errorcode="NoError",
            connectornumber=1,
            statussource="Local"
        )
        assert data.locationid is None
        assert data.evseid is None
        assert data.vendorid is None
        assert data.vendorerrorcode is None

    def test_connectivity_status_changed_data(self):
        """Test ConnectivityStatusChangedData creation and attributes."""
        data = ConnectivityStatusChangedData(status=ChargepointDtoConnectivityStatus.ONLINE)
        assert data.status == ChargepointDtoConnectivityStatus.ONLINE

    def test_session_start_data(self):
        """Test SessionStartData creation and attributes."""
        data = SessionStartData(
            chargepointid="cp123",
            connectornumber=1,
            transactionid="tx123",
            locationid="loc123",
            evseid="evse123",
            stateofcharge=50.0
        )
        assert data.chargepointid == "cp123"
        assert data.connectornumber == 1
        assert data.transactionid == "tx123"
        assert data.locationid == "loc123"
        assert data.evseid == "evse123"
        assert data.stateofcharge == 50.0

    def test_session_update_data(self):
        """Test SessionUpdateData creation and attributes."""
        data = SessionUpdateData(
            chargepointid="cp123",
            connectornumber=1,
            transactionid="tx123",
            totalenergyinkwh=25.5,
            totalduration="PT1H30M",
            totalcosts=15.75,
            locationid="loc123",
            evseid="evse123",
            stateofcharge=75.0
        )
        assert data.chargepointid == "cp123"
        assert data.connectornumber == 1
        assert data.transactionid == "tx123"
        assert data.totalenergyinkwh == 25.5
        assert data.totalduration == "PT1H30M"
        assert data.totalcosts == 15.75
        assert data.locationid == "loc123"
        assert data.evseid == "evse123"
        assert data.stateofcharge == 75.0

    def test_session_stop_data(self):
        """Test SessionStopData creation and attributes."""
        data = SessionStopData(
            chargepointid="cp123",
            connectornumber=1,
            transactionid="tx123",
            totalenergyinkwh=30.0,
            totalduration="PT2H",
            totalcosts=20.0,
            locationid="loc123",
            evseid="evse123",
            stateofcharge=90.0
        )
        assert data.chargepointid == "cp123"
        assert data.connectornumber == 1
        assert data.transactionid == "tx123"
        assert data.totalenergyinkwh == 30.0
        assert data.totalduration == "PT2H"
        assert data.totalcosts == 20.0
        assert data.locationid == "loc123"
        assert data.evseid == "evse123"
        assert data.stateofcharge == 90.0

    def test_cdr_created_data(self):
        """Test CDRCreatedData creation and attributes."""
        data = CDRCreatedData(
            chargepointid="cp123",
            connectornumber=1,
            totalenergyinkwh=25.5,
            totalduration="PT1H30M",
            totalcosts=15.75,
            transactionid="tx123",
            locationid="loc123",
            evseid="evse123"
        )
        assert data.chargepointid == "cp123"
        assert data.connectornumber == 1
        assert data.totalenergyinkwh == 25.5
        assert data.totalduration == "PT1H30M"
        assert data.totalcosts == 15.75
        assert data.transactionid == "tx123"
        assert data.locationid == "loc123"
        assert data.evseid == "evse123"

    def test_empty_data_classes(self):
        """Test data classes that have no fields."""
        location_created = LocationCreatedData()
        location_updated = LocationUpdatedData()
        msp_invoice = MSPInvoiceProposalStatusData()
        ping = PingData()
        
        # These should create instances without errors
        assert isinstance(location_created, LocationCreatedData)
        assert isinstance(location_updated, LocationUpdatedData)
        assert isinstance(msp_invoice, MSPInvoiceProposalStatusData)
        assert isinstance(ping, PingData)


class TestWebhookPayload:
    def test_charge_point_booted_payload(self):
        """Test WebhookPayload with ChargePointBooted data."""
        payload = WebhookPayload(
            specversion="1.0",
            id="test-id",
            type=WebhookPayloadType.ChargePointBooted,
            subject="test-subject",
            time="2024-01-01T00:00:00Z",
            source="test-source",
            datacontenttype="application/json",
            data={"registrationstatus": "Accepted"}
        )
        
        assert isinstance(payload.data, ChargePointBootedData)
        assert payload.data.registrationstatus == RegistrationStatusType.Accepted

    def test_operational_status_changed_payload(self):
        """Test WebhookPayload with OperationalStatusChanged data."""
        payload = WebhookPayload(
            specversion="1.0",
            id="test-id",
            type=WebhookPayloadType.OperationalStatusChanged,
            subject="test-subject",
            time="2024-01-01T00:00:00Z",
            source="test-source",
            datacontenttype="application/json",
            data={
                "status": "Available",
                "errorcode": "NoError",
                "connectornumber": 1,
                "statussource": "Local",
                "locationid": "loc123",
                "evseid": "evse123",
                "vendorid": "vendor123",
                "vendorerrorcode": "vendor_error"
            }
        )
        
        assert isinstance(payload.data, OperationalStatusChangedData)
        assert payload.data.status == ConnectorOperationalStatusDtoOperationalStatus.AVAILABLE
        assert payload.data.errorcode == "NoError"
        assert payload.data.connectornumber == 1
        assert payload.data.statussource == "Local"
        assert payload.data.locationid == "loc123"
        assert payload.data.evseid == "evse123"
        assert payload.data.vendorid == "vendor123"
        assert payload.data.vendorerrorcode == "vendor_error"

    def test_operational_status_changed_payload_with_extra_fields(self):
        """Test WebhookPayload with OperationalStatusChanged data that has extra fields."""
        payload = WebhookPayload(
            specversion="1.0",
            id="test-id",
            type=WebhookPayloadType.OperationalStatusChanged,
            subject="test-subject",
            time="2024-01-01T00:00:00Z",
            source="test-source",
            datacontenttype="application/json",
            data={
                "status": "Available",
                "errorcode": "NoError",
                "connectornumber": 1,
                "statussource": "Local",
                "chargepointid": "cp123",  # Extra field that should be ignored
                "extra_field": "extra_value"  # Another extra field
            }
        )
        
        assert isinstance(payload.data, OperationalStatusChangedData)
        assert payload.data.status == ConnectorOperationalStatusDtoOperationalStatus.AVAILABLE
        assert payload.data.errorcode == "NoError"
        assert payload.data.connectornumber == 1
        assert payload.data.statussource == "Local"
        # Extra fields should be ignored
        assert not hasattr(payload.data, 'chargepointid')
        assert not hasattr(payload.data, 'extra_field')

    def test_connectivity_status_changed_payload(self):
        """Test WebhookPayload with ConnectivityStatusChanged data."""
        payload = WebhookPayload(
            specversion="1.0",
            id="test-id",
            type=WebhookPayloadType.ConnectivityStatusChanged,
            subject="test-subject",
            time="2024-01-01T00:00:00Z",
            source="test-source",
            datacontenttype="application/json",
            data={"status": "Online"}
        )
        
        assert isinstance(payload.data, ConnectivityStatusChangedData)
        assert payload.data.status == ChargepointDtoConnectivityStatus.ONLINE

    def test_session_start_payload(self):
        """Test WebhookPayload with SessionStart data."""
        payload = WebhookPayload(
            specversion="1.0",
            id="test-id",
            type=WebhookPayloadType.SessionStart,
            subject="test-subject",
            time="2024-01-01T00:00:00Z",
            source="test-source",
            datacontenttype="application/json",
            data={
                "chargepointid": "cp123",
                "connectornumber": 1,
                "transactionid": "tx123",
                "locationid": "loc123",
                "evseid": "evse123",
                "stateofcharge": 50.0
            }
        )
        
        assert isinstance(payload.data, SessionStartData)
        assert payload.data.chargepointid == "cp123"
        assert payload.data.connectornumber == 1
        assert payload.data.transactionid == "tx123"
        assert payload.data.locationid == "loc123"
        assert payload.data.evseid == "evse123"
        assert payload.data.stateofcharge == 50.0

    def test_session_update_payload(self):
        """Test WebhookPayload with SessionUpdate data."""
        payload = WebhookPayload(
            specversion="1.0",
            id="test-id",
            type=WebhookPayloadType.SessionUpdate,
            subject="test-subject",
            time="2024-01-01T00:00:00Z",
            source="test-source",
            datacontenttype="application/json",
            data={
                "chargepointid": "cp123",
                "connectornumber": 1,
                "transactionid": "tx123",
                "totalenergyinkwh": 25.5,
                "totalduration": "PT1H30M",
                "totalcosts": 15.75,
                "locationid": "loc123",
                "evseid": "evse123",
                "stateofcharge": 75.0
            }
        )
        
        assert isinstance(payload.data, SessionUpdateData)
        assert payload.data.chargepointid == "cp123"
        assert payload.data.connectornumber == 1
        assert payload.data.transactionid == "tx123"
        assert payload.data.totalenergyinkwh == 25.5
        assert payload.data.totalduration == "PT1H30M"
        assert payload.data.totalcosts == 15.75
        assert payload.data.locationid == "loc123"
        assert payload.data.evseid == "evse123"
        assert payload.data.stateofcharge == 75.0

    def test_session_stop_payload(self):
        """Test WebhookPayload with SessionStop data."""
        payload = WebhookPayload(
            specversion="1.0",
            id="test-id",
            type=WebhookPayloadType.SessionStop,
            subject="test-subject",
            time="2024-01-01T00:00:00Z",
            source="test-source",
            datacontenttype="application/json",
            data={
                "chargepointid": "cp123",
                "connectornumber": 1,
                "transactionid": "tx123",
                "totalenergyinkwh": 30.0,
                "totalduration": "PT2H",
                "totalcosts": 20.0,
                "locationid": "loc123",
                "evseid": "evse123",
                "stateofcharge": 90.0
            }
        )
        
        assert isinstance(payload.data, SessionStopData)
        assert payload.data.chargepointid == "cp123"
        assert payload.data.connectornumber == 1
        assert payload.data.transactionid == "tx123"
        assert payload.data.totalenergyinkwh == 30.0
        assert payload.data.totalduration == "PT2H"
        assert payload.data.totalcosts == 20.0
        assert payload.data.locationid == "loc123"
        assert payload.data.evseid == "evse123"
        assert payload.data.stateofcharge == 90.0

    def test_cdr_created_payload(self):
        """Test WebhookPayload with CDRCreated data."""
        payload = WebhookPayload(
            specversion="1.0",
            id="test-id",
            type=WebhookPayloadType.CDRCreated,
            subject="test-subject",
            time="2024-01-01T00:00:00Z",
            source="test-source",
            datacontenttype="application/json",
            data={
                "chargepointid": "cp123",
                "connectornumber": 1,
                "totalenergyinkwh": 25.5,
                "totalduration": "PT1H30M",
                "totalcosts": 15.75,
                "transactionid": "tx123",
                "locationid": "loc123",
                "evseid": "evse123"
            }
        )
        
        assert isinstance(payload.data, CDRCreatedData)
        assert payload.data.chargepointid == "cp123"
        assert payload.data.connectornumber == 1
        assert payload.data.totalenergyinkwh == 25.5
        assert payload.data.totalduration == "PT1H30M"
        assert payload.data.totalcosts == 15.75
        assert payload.data.transactionid == "tx123"
        assert payload.data.locationid == "loc123"
        assert payload.data.evseid == "evse123"

    def test_location_created_payload(self):
        """Test WebhookPayload with LocationCreated data."""
        payload = WebhookPayload(
            specversion="1.0",
            id="test-id",
            type=WebhookPayloadType.LocationCreated,
            subject="test-subject",
            time="2024-01-01T00:00:00Z",
            source="test-source",
            datacontenttype="application/json",
            data={}
        )
        
        assert isinstance(payload.data, LocationCreatedData)

    def test_location_updated_payload(self):
        """Test WebhookPayload with LocationUpdated data."""
        payload = WebhookPayload(
            specversion="1.0",
            id="test-id",
            type=WebhookPayloadType.LocationUpdated,
            subject="test-subject",
            time="2024-01-01T00:00:00Z",
            source="test-source",
            datacontenttype="application/json",
            data={}
        )
        
        assert isinstance(payload.data, LocationUpdatedData)

    def test_msp_invoice_proposal_status_payload(self):
        """Test WebhookPayload with MSPInvoiceProposalStatus data."""
        payload = WebhookPayload(
            specversion="1.0",
            id="test-id",
            type=WebhookPayloadType.MSPInvoiceProposalStatus,
            subject="test-subject",
            time="2024-01-01T00:00:00Z",
            source="test-source",
            datacontenttype="application/json",
            data={}
        )
        
        assert isinstance(payload.data, MSPInvoiceProposalStatusData)

    def test_ping_payload(self):
        """Test WebhookPayload with Ping data."""
        payload = WebhookPayload(
            specversion="1.0",
            id="test-id",
            type=WebhookPayloadType.Ping,
            subject="test-subject",
            time="2024-01-01T00:00:00Z",
            source="test-source",
            datacontenttype="application/json",
            data={}
        )
        
        assert isinstance(payload.data, PingData)

    def test_webhook_payload_with_already_created_data(self):
        """Test WebhookPayload when data is already a data class instance."""
        existing_data = ChargePointBootedData(registrationstatus=RegistrationStatusType.Accepted)
        
        payload = WebhookPayload(
            specversion="1.0",
            id="test-id",
            type=WebhookPayloadType.ChargePointBooted,
            subject="test-subject",
            time="2024-01-01T00:00:00Z",
            source="test-source",
            datacontenttype="application/json",
            data=existing_data
        )
        
        assert payload.data is existing_data
        assert payload.data.registrationstatus == RegistrationStatusType.Accepted


class TestEdgeCases:
    def test_connectivity_status_case_conversion(self):
        """Test that ConnectivityStatusChanged status is converted to uppercase."""
        payload = WebhookPayload(
            specversion="1.0",
            id="test-id",
            type=WebhookPayloadType.ConnectivityStatusChanged,
            subject="test-subject",
            time="2024-01-01T00:00:00Z",
            source="test-source",
            datacontenttype="application/json",
            data={"status": "online"}  # lowercase
        )
        
        assert isinstance(payload.data, ConnectivityStatusChangedData)
        assert payload.data.status == ChargepointDtoConnectivityStatus.ONLINE

    def test_all_webhook_types_with_extra_fields(self):
        """Test that all webhook types handle extra fields gracefully."""
        webhook_types_and_data = [
            (WebhookPayloadType.ChargePointBooted, {"registrationstatus": "Accepted"}),
            (WebhookPayloadType.OperationalStatusChanged, {
                "status": "Available",
                "errorcode": "NoError", 
                "connectornumber": 1,
                "statussource": "Local"
            }),
            (WebhookPayloadType.ConnectivityStatusChanged, {"status": "Online"}),
            (WebhookPayloadType.SessionStart, {
                "chargepointid": "cp123",
                "connectornumber": 1,
                "transactionid": "tx123"
            }),
            (WebhookPayloadType.SessionUpdate, {
                "chargepointid": "cp123",
                "connectornumber": 1,
                "transactionid": "tx123",
                "totalenergyinkwh": 25.5,
                "totalduration": "PT1H30M",
                "totalcosts": 15.75
            }),
            (WebhookPayloadType.SessionStop, {
                "chargepointid": "cp123",
                "connectornumber": 1,
                "transactionid": "tx123",
                "totalenergyinkwh": 30.0,
                "totalduration": "PT2H",
                "totalcosts": 20.0
            }),
            (WebhookPayloadType.CDRCreated, {
                "chargepointid": "cp123",
                "connectornumber": 1,
                "totalenergyinkwh": 25.5,
                "totalduration": "PT1H30M",
                "totalcosts": 15.75,
                "transactionid": "tx123"
            }),
            (WebhookPayloadType.LocationCreated, {}),
            (WebhookPayloadType.LocationUpdated, {}),
            (WebhookPayloadType.MSPInvoiceProposalStatus, {}),
            (WebhookPayloadType.Ping, {}),
        ]
        
        for webhook_type, base_data in webhook_types_and_data:
            # Add extra fields to the base data
            test_data = {
                **base_data,
                "extra_field_1": "extra_value_1",
                "extra_field_2": "extra_value_2",
                "chargepointid": "should_be_ignored",
                "connectornumber": "should_be_ignored",
                "transactionid": "should_be_ignored"
            }
            
            payload = WebhookPayload(
                specversion="1.0",
                id="test-id",
                type=webhook_type,
                subject="test-subject",
                time="2024-01-01T00:00:00Z",
                source="test-source",
                datacontenttype="application/json",
                data=test_data
            )
            
            # Should not raise any exceptions
            assert payload.data is not None
            # Extra fields should not be present
            assert not hasattr(payload.data, 'extra_field_1')
            assert not hasattr(payload.data, 'extra_field_2') 