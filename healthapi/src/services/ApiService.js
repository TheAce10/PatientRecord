import axios from "axios";

export function getPatient(){
    return axios.get('http://127.0.0.1:8000/api/patient/')
    .then(res => {
        return res.data
    })
}

export function addPatient(patient){
    return axios.post('http://127.0.0.1:8000/api/patient/',
    {
        patient_id:null,
        first_name: patient.first_name.value,
        last_name: patient.last_name.value,
        blood: patient.blood.value,
    }
    )
    .then(res => {
        return res.data
    })
}