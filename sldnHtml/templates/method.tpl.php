<?= $this->render('header.tpl.php'); ?>
        <div class="section clearfix">
        <div id="main-wrapper">
            <div id="main" class="clearfix">
                <?= $this->render('sidebar.tpl.php'); ?>
                <div id='content' class='inner-content'>
                    <h1 class='title' id='page-title'> 
                        <div id='title-category'><?= $this->category?> </div>
                        <div id='title-full'><?=$this->parent?>::<?= $this->title ?></div>
                    </h1>
                    <h2> Overview </h2>
                    <?= $this->body ?>
                    <h3>Parameters </h3>
                    <div id="parameters  ">
                        <table class="view-content" id="method-param-table">
                            <tbody>
                            <?php $even = 'even'; ?>
                            <?php foreach($this->parameters as $param): ?>
                                <tr class="method-param-tr <?=$even?>">
                                    <td> <?= $param->title ?> </td>
                                    <td> <?= $this->print_property_type($param->sldnType, $param->isArray)?> </td>
                                    <td> <?= $param->body ?> </td>
                                </tr>
                            <?php if($even == 'even'): { $even = 'odd';} else: {$even = 'even';} endif?>
                            <?php endforeach ?>
                            </tbody>
                        </table>
                    </div>

                    <h3> Required Headers </h3>
                        <?php foreach($this->requiredHeaders as $key => $value): ?>
                            <div class="method-headers method-data"> <?= $value ?></div>
                        <?php endforeach ?>
                    <h3> Optional Headers </h3>
                        <?php foreach($this->optionalHeaders as $key => $value): ?>
                            <div class="method-headers method-data"><?= $value ?></div>
                        <?php endforeach ?>
                    <h3> Return Values </h3>
                    <div class="method-data">
                            <?= $this->print_property_type($this->returnValue, $this->isArray)?>
                    </div>
                    Last Updated <?= date('r', $this->changed) ?>
                    <pre style="display:none;"><?print_r($this)?></pre>
                </div>
            </div>
    </div>
</div>
    </body>
</html>