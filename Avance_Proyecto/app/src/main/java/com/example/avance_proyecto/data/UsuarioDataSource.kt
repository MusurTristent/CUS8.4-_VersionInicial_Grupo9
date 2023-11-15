package com.example.avance_proyecto.data

import com.example.avance_proyecto.R
import com.example.avance_proyecto.data.uistate.UsuarioUiState

object UsuarioDataSource {

    var usuarios = listOf<UsuarioUiState>(
        UsuarioUiState(
            nombrecompleto = R.string.nombrecompletoX,
            puesto = R.string.puestoX,
            predio = R.string.predioX,
            ubicacion = R.string.ubicacionX,
            tiempo = R.string.tiempoX,
            data = "Carlos Rodriguez"/*,
            imageRes = R.drawable.android_superhero1*/
        )
    )

}