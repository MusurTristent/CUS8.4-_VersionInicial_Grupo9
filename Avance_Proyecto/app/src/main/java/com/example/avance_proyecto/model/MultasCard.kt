package com.example.avance_proyecto.model

import androidx.annotation.DrawableRes
import androidx.compose.ui.graphics.Color
import com.example.avance_proyecto.data.model.ConteoEstadoSolicitudItem

data class MultasCard(
    @DrawableRes val imageRes: Int,
    val lightColor: Color,
    val mediumColor: Color,
    val darkColor: Color,
    val conteoSolicitudItems: ConteoEstadoSolicitudItem
)
