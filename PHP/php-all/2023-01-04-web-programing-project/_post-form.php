<!-- Formular zur Erstellung als auch Bearbeitung eines Blog -Artikels -->
<form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="post">
    
<div class="mb-3">
    <!-- Ausgabe der Blog-Kategorien -->
    <select name="categ_id" class="form-select">
        <optgroup label="Kategorie">

            <?php 
            $sql = 'SELECT * FROM  `tbl_categories`;';
            $stmt = $db->query( $sql );
            while( $row = $stmt->fetch() ): 
                $selected = '';
                if( $row['categ_id'] === $categ_id ) $selected = 'selected';
            ?>

                <option value="<?= $row['categ_id']; ?>"><?= $row['categ_name']; ?></option>

             <?php endwhile ?> 

            </optgroup>
    </select>
</div>





<div class="mb-3">
            <label for="post"class="form-label">Title</label>
            <input type="text" name="posts_header" id="posts_header" class="form-control" value="<?= htmlspecialchars( $post_header );?>">


</div>




    <div class="mb-3">
                <label for="post_body" class="form">Text</label>
                <textarea name="posts_body" id="posts_body" cols="30" rows="10" class="form-control"><?= nl2br( htmlspecialchars( $post_body) ); ?></textarea>
    </div>




    <div calss="mb-3">
            <label for="posts_img">bild zum Artikel </label>
            <input type="file" name="posts_img" id="posts_img" class="form-control">

    </div>

<div class="mb-3">
                <label for="posts_img_alt">Alternative Bildbezeichnung</label>
                <input type="text" name="posts_img_alt" id="posts_img_alt" class="form-control" value="<?= ($post_img_alt ?? '' ) ; ?>">
</div>



                <!-- Falls vorhanden, Artikel-ID versteckt übermitteln (notwendig bei bearbeitung) -->
                <input type="hidden" name="posts_id" value="<?= $post_id; ?>">

                <!-- Abbruch einer Bearbeitung führt zum Artikel, Abbruch einer Neuerstellung zur Startseite -->
                <a href="<?= isset( $post_id)? '05-post.php?post_id=' . $post_id : '04-index.php'; ?>" class="btn btn-outline-secondary">abbrechen</a>

                <button class="submit btn btn-primary">Veröffentlichen</button>



</form>