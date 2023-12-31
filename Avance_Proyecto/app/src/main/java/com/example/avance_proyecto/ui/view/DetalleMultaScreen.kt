package com.example.avance_proyecto.ui.view

import android.content.Context
import android.widget.Toast
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.LazyRow
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ArrowBack
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Card
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBar
import androidx.compose.material3.TopAppBarDefaults
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.window.DialogProperties
import androidx.navigation.NavController
import androidx.navigation.compose.rememberNavController
import com.example.avance_proyecto.data.MultasDefaultDataSource
import com.example.avance_proyecto.ui.theme.ButtonColorDefault
import com.example.avance_proyecto.ui.theme.ButtonColorRed
import com.example.avance_proyecto.ui.theme.TextWhite
import com.example.avance_proyecto.ui.theme.backgroundPrincipal

@Composable
fun DetalleMultaScreen(
    navController: NavController
){
    val multas = MultasDefaultDataSource.itemCardInformation

    Scaffold(
        topBar = {
            MultasAppBarInformation(
                navigateUp = { navController.navigateUp() }
            )
        }
    ){ innerPadding ->
        LazyColumn(
            modifier = Modifier
                .padding(innerPadding)
                .background(backgroundPrincipal)
                .fillMaxSize()
        ) {
            items(1) {
                multas.forEach { it->
                    CardInformation(label = stringResource(it.labelData) , data = it.valueData.toString())
                }
                ButtonSectionDetails(listOf("Anular", "Pagar"), "Opciones a realizar:")
                //ButtonSectionOption(listOf("Cotizar", "Observar", "Anular"), "Seleccionar opción:")
            }
        }
    }

}

@Composable
fun CardInformation(label: String, data: String){
    Card(
        modifier = Modifier.padding(vertical = 8.dp, horizontal = 16.dp)
    ){
        Row(
            modifier = Modifier
                .padding(16.dp)
                .fillMaxWidth(),
            verticalAlignment = Alignment.CenterVertically,
            horizontalArrangement = Arrangement.SpaceBetween
        ) {
            Text(
                text= label,
                style = MaterialTheme.typography.labelLarge,
                fontWeight = FontWeight.Bold,
                modifier = Modifier.padding(end=16.dp)
            )
            Text(text = data)
        }

    }


}

@Composable
fun MultasAppBarInformation(
    navigateUp: () -> Unit
){
    TopAppBar(
        modifier = Modifier.background(backgroundPrincipal),
        title = {
            Row(
                modifier = Modifier.fillMaxSize(),
                verticalAlignment = Alignment.CenterVertically,
                horizontalArrangement = Arrangement.SpaceBetween
            ) {
                Text(
                    text = "Detalle de la Multa",
                    color = Color.White,
                    fontWeight = FontWeight.Bold
                )

            }


        },
        colors = TopAppBarDefaults.mediumTopAppBarColors(
            containerColor = backgroundPrincipal
        ),
        navigationIcon = {
            IconButton(onClick = navigateUp) {
                Icon(
                    imageVector = Icons.Filled.ArrowBack,
                    contentDescription = "Back",
                    tint = Color.White
                )
            }
        }
    )
}



@Composable
fun ButtonSectionDetails(
    botones: List<String>, title: String
) {
    val context = LocalContext.current
    //val gameUiState by popUpViewModel.uiState.collectAsState()

    var selectedButtonIndex by remember {
        mutableStateOf(0)
    }

    var showDialog by remember {
        mutableStateOf(false)
    }

    Column(
        modifier = Modifier.padding(vertical = 8.dp, horizontal = 16.dp)
    ){
        Text(
            text=title,
            color= Color.White,
            modifier = Modifier.padding(bottom=10.dp)
        )
        LazyRow(
            modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.SpaceEvenly
        ) {
            items(botones.size) {
                Button(
                    onClick = {
                        showToastInformation(context, botones[it])
                        selectedButtonIndex = it
                        showDialog = true
                    },
                    colors = ButtonDefaults.buttonColors(
                        ButtonColorDefault,
                        Color.White
                    ),
                    shape = MaterialTheme.shapes.small
                ) {
                    Text(text = botones[it], color = TextWhite)
                }
            }
        }
    }

    if(showDialog && selectedButtonIndex == 0){
        InformacionAreasComunesScreen(
            onDimiss = { showDialog = false }
        )
    }
    if(showDialog && selectedButtonIndex == 1){
        SolicitanteContent(
            onDimiss = { showDialog = false }
        )
    }

}

@Composable
fun ButtonSectionOption(
    botones: List<String>, title: String
) {
    val context = LocalContext.current
    //val gameUiState by popUpViewModel.uiState.collectAsState()

    var selectedButtonIndex by remember {
        mutableStateOf(0)
    }

    var showDialog by remember {
        mutableStateOf(false)
    }

    Column(
        modifier = Modifier.padding(vertical = 8.dp, horizontal = 16.dp)
    ){
        Text(
            text=title,
            color= Color.White,
            modifier = Modifier.padding(bottom=10.dp)
        )
        LazyRow(
            modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.SpaceEvenly
        ) {
            items(botones.size) {
                Button(
                    onClick = {
                        showToastInformation(context, botones[it])
                        selectedButtonIndex = it
                        showDialog = true
                    },
                    colors = ButtonDefaults.buttonColors(
                        if (botones[it] == "Anular") {
                            ButtonColorRed
                        } else {
                            ButtonColorDefault
                        },
                        Color.White
                    ),
                    shape = MaterialTheme.shapes.small
                ) {
                    Text(text = botones[it], color = TextWhite)
                }
            }
        }
    }

    if(showDialog && selectedButtonIndex == 2){
        AnulacionScreen(
            onDimiss = { showDialog = false },
            onPositiveButtonClicked = { showDialog = false },
            onNegativeButtonClicked = { showDialog = false },
            properties = DialogProperties(
                dismissOnBackPress = false,
                dismissOnClickOutside = false
            )
        )
    }
}

fun showToastInformation(context: Context, message: String) {
    Toast.makeText(context, message, Toast.LENGTH_SHORT).show()
}
@Preview
@Composable
fun DetalleMultaScreenPreview() {
    val navController = rememberNavController() // Importa rememberNavController
    DetalleMultaScreen(navController = navController)
}