package com.example.avance_proyecto.data

import com.example.avance_proyecto.R
import com.example.avance_proyecto.data.model.ConteoEstadoSolicitudItem
import com.example.avance_proyecto.data.uistate.InformationCardUiState
import com.example.avance_proyecto.model.MultasCard
import com.example.avance_proyecto.ui.theme.*

object MultasDefaultDataSource {

    val itemCardMultas = listOf(
        MultasCard(R.drawable.pendiente_image,//Pendiente
            BlueViolet1,
            BlueViolet2,
            BlueViolet3,
            ConteoEstadoSolicitudItem(0,"Pendiente")
        ),
        MultasCard(
            R.drawable.cotizado_image,//Cotizado
            LightGreen1,
            LightGreen2,
            LightGreen3,
            ConteoEstadoSolicitudItem(0,"Cotizado")
        ),
        MultasCard(
            R.drawable.observado_image,//Observado
            OrangeYellow1,
            OrangeYellow2,
            OrangeYellow3,
            ConteoEstadoSolicitudItem(0,"Observado")
        ),
        MultasCard(
            R.drawable.anulado_image,//Anulado
            Beige1,
            Beige2,
            Beige3,
            ConteoEstadoSolicitudItem(0,"Anulado")
        )
    )

    val itemCardDataStaticMultas = listOf(
        ConteoEstadoSolicitudItem(
            0,
            "Pendientes"
        )
    )

    val itemCardInformation = listOf(
        InformationCardUiState(
            R.string.ap_paterno,"Salas"
        ),
        InformationCardUiState(
            R.string.ap_materno,"Ramirez"
        ),
        InformationCardUiState(
            R.string.nombres,"Marcelo"
        ),
        InformationCardUiState(
            R.string.codigo,"A3"
        ),
        InformationCardUiState(
            R.string.importe,"S/200.00"
        ),
        InformationCardUiState(
            R.string.descripcion,"Colgar ropa"
        ),
        InformationCardUiState(
            R.string.fecha_infraccion,"2002-06-20"
        ),
        InformationCardUiState(
            R.string.periodo,"Semana"
        )
    )

}