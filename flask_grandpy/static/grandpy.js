// Index map
var response_count = 0;
// Importation du script Javascript Maps API
var script_map = true;


$(document).ready(function() {

    // Validation du formulaire par appui de la touche 'Entrée'
    $("form").submit(function(e) {
        e.preventDefault(e);
    });
    $("#message").keypress(function(e) {
        if (e.which == 13) {
            $("#Submit").click();
        }
    });

    // Action lors de l'envoi du formulaire AJAX
    $('#Submit').on('click', function() {
        // Question posée par l'utilisateur
        $("#discussion").append(`
            <div class="row justify-content-end mb-2">
                <div class="col-8">
                    <div class="card-user p-3">
                        <p>
                            ` + $("#message").val() + `
                        </p>
                    </div>
                </div>
            </div>
        `);
        // Message indiquant que la recherche est en cours
        $("#discussion").append(`
            <div class="row justify-content-start mb-2" id="loading_card">
                <div class="col-8">
                    <div class="card-grandpy p-3">
                        <p id="loading">GrandPy est en train d'écrire <span>.</span><span>.</span><span>.</span></p>
                    </div>
                </div>
            </div>
        `);
        var form = $("form");
        response_count ++;
        // Méthode AJAX
        $.ajax({
            url: form.attr("data-show-response"),
            data: form.serialize(),
            dataType: 'json',
            method: "POST",
            success: function (data) {
                // Suppression du message recherche en cours
                $("#loading_card").remove();

                // Réponse normale de GrandPy si aucune erreur dans la recherche des données
                if (data.error == null) {

                    // Réponse GrandPy 1 : Adresse du lieu recherché
                    $("#discussion").append(`
                        <div class="row justify-content-start mb-2">
                            <div class="col-8">
                                <div class="card-grandpy p-3">
                                    <p>` + data.grandpy_adresse + `</p>
                                </div>
                            </div>
                        </div>
                    `);

                    // Réponse GrandPy 2 : map
                    var gmap_id = "gmap" + response_count;
                    $("#discussion").append(`
                        <div class="row justify-content-start mb-2">
                            <div class="col-8">
                                <div class="card-grandpy p-3">
                                    <p>
                                        ` + data.grandpy_map + `
                                    </p>
                                    <div id="` + gmap_id + `" class="gmap"></div>
                                </div>
                            </div>
                        </div>
                    `);

                    // Visualisation du lieu cherché JS API MAP
                    var positions = data.location;
                    var center = positions[0];
                    if (script_map) {

                        // Initialisation de la carte
                        initMap = function() {
                            // Définition de la carte
                            var gmap = new google.maps.Map(
                                document.getElementById(gmap_id),
                                {zoom:12, center: center}
                            );
                            // Ajout de chaque lieu trouvé
                            for (var i = 0; i < positions.length; i++) {
                                // Marqueur pour chaque lieu
                                var marker = new google.maps.Marker({
                                    position: new google.maps.LatLng(positions[i].lat, positions[i].lng),
                                    map: gmap,
                                    title: positions[i].name
                                });
                                // Information sur chaque lieu
                                const infowindow = new google.maps.InfoWindow({
                                    content: positions[i].content
                                });
                                marker.addListener("click", () => {
                                    infowindow.open(
                                        gmap,
                                        marker
                                    );
                                });
                            }
                        }
                        // Ajout du script JS API MAP
                        var script_tag = document.createElement('script');
                        script_tag.setAttribute(
                            "src",
                            data.link_js
                        );
                        $("head").append(script_tag);
                        script_map = false;
                    } else {
                        // Initialisation de la nouvelle carte
                        var gmap = new google.maps.Map(
                            document.getElementById(gmap_id),
                            {zoom:12, center: center}
                        );
                        // Ajout de chaque marqueur de la nouvelle recherche
                        for (var i = 0; i < positions.length; i++) {
                            var marker = new google.maps.Marker({
                                position: new google.maps.LatLng(positions[i].lat, positions[i].lng),
                                map: gmap,
                                title: positions[i].name
                            });
                            const infowindow = new google.maps.InfoWindow({
                                content: positions[i].content
                            });
                            marker.addListener("click", () => {
                                infowindow.open(
                                    gmap,
                                    marker
                                );
                            });
                        }
                    }

                    // Réponse GrandPy 3 : Wiki
                    $("#discussion").append(`
                        <div class="row justify-content-start mb-2">
                            <div class="col-8">
                                <div class="card-grandpy p-3">
                                    <h6>
                                        ` + data.wiki_title + `
                                    </h6>
                                    <p>
                                        <dl>` + data.grandpy_wiki + `</dl>
                                    </p>
                                </div>
                            </div>
                        </div>
                    `);

                    // Réponse GrandPy 4 : Message informations supplémentaires
                    $("#discussion").append(`
                        <div class="row justify-content-start mb-2">
                            <div class="col-8">
                                <div class="card-grandpy p-3">
                                    <p>Alors, content ? Veux-tu que je te parles d'un autre lieu ?</p>
                                </div>
                            </div>
                        </div>
                    `);
                } else {

                    // Suppression du message recherche en cours
                    $("#loading_card").remove();

                    // Réponse de GrandPy si erreur dans la recherche du lieu demandé
                    $("#discussion").append(`
                        <div class="row justify-content-start mb-2">
                            <div class="col-8">
                                <div class="card-grandpy p-3">
                                    <p>
                                        ` + data.error + `
                                    </p>
                                </div>
                            </div>
                        </div>
                    `);
                }

                // Réinitialisation de la zone de texte utilisateur
                $("#message").val('');
            }
        });
    });
    window.google = {};
});