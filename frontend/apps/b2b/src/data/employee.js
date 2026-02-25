import { createResource } from "frappe-ui"
import router from "@/router"

export const employeeResource = createResource({
    url: "hrms.api.get_current_employee_info",
    cache: "hrms:employee",
    onError(error) {
        if (error && error.exc_type === "AuthenticationError") {
            router.push("/login")
        }
    },
})
