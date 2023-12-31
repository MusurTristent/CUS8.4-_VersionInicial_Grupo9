package com.example.avance_proyecto.ui.viewmodel

import androidx.lifecycle.ViewModel
import com.example.avance_proyecto.data.uistate.MultasUiState
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow

class OrderViewModel : ViewModel() {

    private val _uiState = MutableStateFlow(MultasUiState())
    val uiState: StateFlow<MultasUiState> = _uiState.asStateFlow()

    /* recuperar datos de la base de datos */
}