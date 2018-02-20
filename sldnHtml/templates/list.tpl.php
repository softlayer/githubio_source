<?php foreach($this->objects as $item): ?>
<div class='list-row'>
    <div class='list-row-title'><a href='/reference/<?= $this->type ?>/<?= $item ?>'> <?=  str_replace('SoftLayer_', '', $item) ?></a></div>
</div>
<?php endforeach ?>