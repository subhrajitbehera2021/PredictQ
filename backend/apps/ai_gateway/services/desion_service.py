from ai_gateway.models import DecisionLog


class GatewayService:

    @staticmethod
    def log_decision(hospital, user, action_type, input_data, output_data):

        return DecisionLog.objects.create(
            hospital=hospital,
            user=user,
            action_type=action_type,
            input_data=input_data,
            output_data=output_data
        )